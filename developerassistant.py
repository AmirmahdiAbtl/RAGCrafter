import os
import sqlite3
from datetime import datetime
from flask import Blueprint, render_template, request, jsonify
from langchain.prompts import PromptTemplate
from utils import get_retrieval_chain, get_llm, developer_summarize_chat_history

developerassistant_bp = Blueprint('developerassistant', __name__)
llm = get_llm()

@developerassistant_bp.route("/", methods=["GET", "POST"])
def generate_story():
    if request.method == "POST":
        try:
            user_input = request.form.get('userInput', '').strip()
            chat_id = request.form.get('chat_id', None)

            # Use a single query to handle both existing and new chat sessions
            summary = ""
            pending_text = ""
            with sqlite3.connect('database.db') as conn:
                cursor = conn.cursor()

                # Attempt to retrieve existing chat
                cursor.execute(
                    '''SELECT id, summary, pending_text
                       FROM chat_developerassistant
                       WHERE id = ?''',
                    (chat_id,)
                )
                existing_chat = cursor.fetchone()

                # If not found, create it
                if not existing_chat:
                    model_name = "llama-3.3-70b-versatile"
                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    chat_name = user_input[:50] if len(user_input) > 50 else user_input

                    summary = user_input
                    cursor.execute(
                        '''INSERT INTO chat_developerassistant (name, summary, language_model, start_chat, pending_text)
                           VALUES (?, ?, ?, ?, ?)''',
                        (chat_name, summary, model_name, timestamp, "")
                    )
                    chat_id = cursor.lastrowid
                else:
                    # Retrieve existing summary and pending_text
                    _, summary, pending_text = existing_chat

                # Append new user input to pending_text
                pending_text += f"\nUser: {user_input}"

                # Build retrieval chain with summary and pending_text
                prompt_template = PromptTemplate(
                    input_variables=["context", "question", "chat_history"],
                    template="""
                        This is the summary of our chat: {chat_history}

                        You are a helpful AI assistant that answers strictly based on the provided documentation. Your job is to help the user understand the libraries and their functionalities, and generate code if applicable. Here's how you should respond:
                        
                        - If the user asks about **installation instructions** or **how to use** a library or feature, provide a clear answer based on the documentation.
                        - If the user asks for **code examples**, generate code based on the relevant documentation, providing the correct syntax and functions, where applicable.
                        - If the user asks a question that is **clearly answered in the provided documentation** or in our previous chat history, respond directly and accurately based on that information.
                        - If the answer **can be reasonably inferred** (e.g., common usage patterns, general practices for a library), provide a general response that is still grounded in the documentation.
                        - If the topic is **completely unrelated** to the documentation, respond with:
                        *\"I couldn't find that in the provided documentation.\"*

                        ### **Documentation Context:**
                        {context}

                        ### **User Question:**
                        {question}
                    """
                )
                retrieval_chain = get_retrieval_chain(prompt_template, "faiss_index_ml")
                full_chat_history = summary + "\n" + pending_text

                result = retrieval_chain({
                    "question": user_input,
                    "chat_history": [(full_chat_history, "Previous Summary")]
                })
                response = result["answer"]

                # Append assistant response
                pending_text += f"\nAssistant: {response}"

                # If pending_text is too large, summarize everything
                if len(pending_text) > 5000:
                    full_text = summary + "\n" + pending_text
                    summary = developer_summarize_chat_history(full_text)
                    pending_text = ""

                # Store changes in a single transaction
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                cursor.execute(
                    '''UPDATE chat_developerassistant
                       SET summary = ?, pending_text = ?
                       WHERE id = ?''',
                    (summary, pending_text, chat_id)
                )
                cursor.execute(
                    '''INSERT INTO chat_detail_developerassistant (chat_id, prompt, chat_response, time)
                       VALUES (?, ?, ?, ?)''',
                    (chat_id, user_input, response, timestamp)
                )
                conn.commit()

            return jsonify({"response": response, "chat_id": chat_id})

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    # If GET, fetch all existing chats
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM chat_developerassistant ORDER BY start_chat DESC')
        chats = cursor.fetchall()

    return render_template("developerassistant.html", chats=chats)


@developerassistant_bp.route("/chat/<int:chat_id>", methods=["GET"])
def get_chat(chat_id):
    """Fetch chat history by chat_id."""
    try:
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute(
                '''SELECT name FROM chat_developerassistant
                   WHERE id = ?''',
                (chat_id,)
            )
            chat_name = cursor.fetchone()

            cursor.execute(
                '''SELECT prompt, chat_response
                   FROM chat_detail_developerassistant
                   WHERE chat_id = ?
                   ORDER BY time ASC''',
                (chat_id,)
            )
            chat_details = cursor.fetchall()

        if chat_name is None:
            return jsonify({"error": "Chat not found"}), 404

        return jsonify({"chat_name": chat_name[0], "chat_details": chat_details})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@developerassistant_bp.route("/new_chat", methods=["POST"])
def new_chat():
    """Create and return a new empty chat session."""
    try:
        model_name = "llama-3.3-70b-versatile"
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        chat_name = f"New Session"

        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute(
                '''INSERT INTO chat_developerassistant (name, summary, language_model, start_chat, pending_text)
                   VALUES (?, ?, ?, ?, ?)''',
                (chat_name, "", model_name, timestamp, "")
            )
            chat_id = cursor.lastrowid
            conn.commit()

        return jsonify({"chat_id": chat_id, "chat_name": chat_name})
    except Exception as e:
        return jsonify({"error": str(e)}), 500