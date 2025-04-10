import os
import sqlite3
from datetime import datetime
from flask import Blueprint, render_template,redirect, url_for, request, jsonify
from langchain.prompts import PromptTemplate
from utils import get_retrieval_chain, get_llm, generate_embedding, name_generator
import numpy as np
import json
from langchain import LLMChain
from database import get_rag, get_rag_documents, create_chat_session, get_chat_sessions_for_rag, get_rag_documents, update_rag
regular_bp = Blueprint('regular', __name__)

@regular_bp.route("/", methods=["GET", "POST"])
def generate_story():
    if request.method == "POST":
        try:
            user_input = request.form.get('userInput', '').strip()
            chat_id = request.form.get('chat_id', None)
            rag_id = request.form.get('rag_id', None)
            # print(f"Received input: {user_input}, chat_id: {chat_id}, rag_id: {rag_id}")
            if not user_input:
                # print("No input provided")
                return jsonify({"error": "No input provided"}), 400
                
            if not chat_id and not rag_id:
                return jsonify({"error": "Either chat_id or rag_id must be provided"}), 400
            
            # print(f"Processing input for chat_id={chat_id}, rag_id={rag_id}")

            with sqlite3.connect('database.db') as conn:
                cursor = conn.cursor()

                # Attempt to retrieve existing chat
                cursor.execute(
                    '''SELECT id FROM chat_season
                       WHERE id = ?''',
                    (chat_id,)
                )
                existing_chat = cursor.fetchone()
                
                # If not found, create it
                if not existing_chat:
                    model_name = "llama-3.3-70b-versatile"
                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    chat_name = user_input[:50] if len(user_input) > 50 else user_input
                    cursor.execute(
                        '''INSERT INTO chat_season (rag_id, name, language_model, start_chat)
                           VALUES (?, ?, ?, ?)''',
                        (rag_id, chat_name, model_name, timestamp)
                    )
                    chat_id = cursor.lastrowid
                   
                # Retrieve existing chat history
            with sqlite3.connect('database.db') as conn:
                cursor = conn.cursor()
                cursor.execute(
                    '''SELECT prompt, chat_response, embedding
                       FROM chat_detail
                       WHERE chat_id = ?
                       ORDER BY time ASC''',
                    (chat_id,)
                )
                rag = get_rag(rag_id)
                chat_history_rows = cursor.fetchall()
                print(f"Chat history rows: {len(chat_history_rows)}")
                if len(chat_history_rows) == 0:
                    sug_name = name_generator(rag["model_type"], rag["model_name"], user_input, rag["api_key"])
                    print(sug_name)
                    with sqlite3.connect('database.db') as conn:
                        cursor = conn.cursor()
                        query = '''UPDATE chat_season SET name = ? WHERE id = ?'''
                        values = (sug_name, chat_id)
                        cursor.execute(query, values)
                        conn.commit()
                    print(f"Chat name updated to: {sug_name}")    
                # Format chat history (only the prompt and response are used in final chain)
                formatted_chat_history = []
                for row in chat_history_rows:
                    prompt = row[0]
                    # row[1] is the stored OpenAPI content (ignored when creating the final prompt text, but kept in DB)
                    response = row[1]
                    formatted_chat_history.append((prompt, response))

                similarities = []
                query_embedding = generate_embedding(user_input)
                for row in chat_history_rows:
                    db_embedding_bytes = json.loads(row[2])
                    # Compute cosine similarity
                    numerator = float(np.dot(query_embedding, db_embedding_bytes))
                    denominator = float(np.linalg.norm(query_embedding) * np.linalg.norm(db_embedding_bytes) + 1e-8)
                    similarity = numerator / denominator
                    similarities.append({
                        "prompt": row[0],
                        "response": row[1],
                        "similarity": similarity
                    })
                sorted_results = sorted(similarities, key=lambda x: x["similarity"], reverse=True)
                top_3 = sorted_results[:3]

                for item in top_3:
                    formatted_chat_history.append((item['prompt'], item['response']))

                
                prompt_template = PromptTemplate(
                    input_variables=["chat_history", "question"],
                    template="""
                    This is the summary of our chat: {chat_history}
                    You are a regular Chat Bot and use the chat history as memory of the previous chat has been done.
                    question : {question}
                    """
                )
                llm = get_llm(rag["model_name"], rag["api_key"], rag["model_type"])
                chat_chain = LLMChain(llm=llm, prompt=prompt_template) 

                response = chat_chain.run(chat_history=formatted_chat_history, question=user_input)

                embedding_vec = generate_embedding(f"{response}, {user_input}")
                embedding_json = json.dumps(embedding_vec)

                # Store changes in a single transaction
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                with sqlite3.connect('database.db') as conn:
                    cursor = conn.cursor()
                    cursor.execute(
                        '''INSERT INTO chat_detail
                        (chat_id, prompt, chat_response, time, embedding)
                        VALUES (?, ?, ?, ?, ?)''',
                        (chat_id, user_input, response, timestamp, embedding_json)
                    )
                    conn.commit()

            return jsonify({"response": response, "chat_id": chat_id})

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    # If GET, fetch all existing chats
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM chat_season ORDER BY start_chat DESC')
        chats = cursor.fetchall()

    return render_template("developerassistant.html", chats=chats, rag_id = rag_id)

@regular_bp.route('/model-selection', methods=['GET', 'POST'])
def model_selection(rag_id):
    if request.method == 'POST':
        model_type = request.form.get('model_type')
        model_name = request.form.get('model_name')
        api_key = request.form.get('api_key')
        
        update_data = {
            'model_type': model_type,
            'model_name': model_name,
            'api_key': api_key,
        }
        print(update_data)
        update_rag(0, update_data, 'created')
        
        # Move to the next phase
        return redirect(url_for('rag_creator.db_embedding_selection', rag_id=rag_id))
    
    # If GET, show the model selection form
    rag = get_rag(rag_id)
    return render_template('model_selection.html', rag=rag)

@regular_bp.route('/chat/<int:rag_id>', methods=["GET"])
def chat_with_rag(rag_id):
    """Start a chat with a specific RAG application"""
    try:
        # Get RAG details
        rag = get_rag(rag_id)
        if not rag:
            print(f"RAG application with ID {rag_id} not found")
            return render_template("error.html", error="RAG application not found"), 404
            
        # Check if RAG is ready
        if rag.get('status') != 'ready':
            return render_template("error.html", error="This RAG application is not fully configured yet. Please complete all setup steps first."), 400
        
        print(f"Fetching chat sessions for RAG ID {rag_id}")
        
        # Get existing chat sessions for this RAG
        try:
            chat_sessions = get_chat_sessions_for_rag(rag_id)
            print(f"Found {len(chat_sessions)} existing chat sessions")
            
            # Format chat_sessions to match what the template expects
            formatted_sessions = []
            for session in chat_sessions:
                formatted_sessions.append([
                    session['id'],  # chat_id
                    session['rag_id'],  # rag_id
                    session['name'],  # chat_name
                    session['language_model'],  # model_name
                    session['start_chat']  # timestamp
                ])
        except Exception as session_error:
            print(f"Error getting chat sessions: {str(session_error)}")
            formatted_sessions = []
        
        # Create an empty chat if none exists
        if not formatted_sessions:
            try:
                print("No existing chat sessions, creating an initial one")
                # Create initial chat session
                model_name = rag.get('model_name', "default-model")
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                chat_name = f"Initial Session - {timestamp}"
                
                chat_id = create_chat_session(rag_id, chat_name, model_name, timestamp)
                print(f"Created new chat session with ID {chat_id}")
                
                formatted_sessions = [[
                    chat_id,  # chat_id
                    rag_id,  # rag_id
                    chat_name,  # chat_name
                    model_name,  # model_name
                    timestamp  # timestamp
                ]]
            except Exception as create_error:
                # print(f"Error creating initial chat: {str(create_error)}")
                return render_template("error.html", error=f"Could not create chat session: {str(create_error)}"), 500
        
        # print(f"Rendering template with RAG ID {rag_id} and {len(formatted_sessions)} chat sessions")
        return render_template("developerassistant.html", rag=rag, chats=formatted_sessions, rag_id=rag_id)
    
    except Exception as e:
        print(f"Error in chat_with_rag: {str(e)}")
        import traceback
        traceback.print_exc()
        return render_template("error.html", error=str(e)), 500



@regular_bp.route("/chat_history/<int:chat_id>", methods=["GET"])
def get_chat(chat_id):
    """Fetch chat history by chat_id."""
    try:
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute(
                '''SELECT name, rag_id FROM chat_season
                   WHERE id = ?''',
                (chat_id,)
            )
            chat_info = cursor.fetchone()

            cursor.execute(
                '''SELECT prompt, chat_response
                   FROM chat_detail
                   WHERE chat_id = ?
                   ORDER BY time ASC''',
                (chat_id,)
            )
            chat_details = cursor.fetchall()

        if chat_info is None:
            return jsonify({"error": "Chat not found"}), 404

        # Return the required data structure expected by the template
        return jsonify({
            "chat_id": chat_id,
            "chat_name": chat_info[0], 
            "rag_id": chat_info[1], 
            "chat_details": chat_details
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@regular_bp.route("/new_chat", methods=["POST"])
def new_chat():
    """Create and return a new empty chat session."""
    try:
        rag_id = request.form.get('rag_id')
        if not rag_id:
            return jsonify({"error": "RAG ID is required"}), 400
            
        # Get model from RAG application
        rag = get_rag(rag_id)
        if not rag:
            return jsonify({"error": "RAG application not found"}), 404
            
        model_name = rag.get('model_name', "llama-3.3-70b-versatile")
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        chat_name = f"New Session - {timestamp}"

        chat_id = create_chat_session(rag_id, chat_name, model_name, timestamp)

        return jsonify({
            "chat_id": chat_id, 
            "chat_name": chat_name,
            "rag_id": rag_id,
            "model_name": model_name
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500