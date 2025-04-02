from langchain_huggingface import HuggingFaceEmbeddings
from config import EMBEDDING_MODEL_NAME, GROQ_API_KEY, LLM_MODEL_NAME
import os
from groq import Groq
from langchain_community.vectorstores import FAISS
# from embeddings import get_embedding_model
from langchain_groq import ChatGroq
from langchain.chains import ConversationalRetrievalChain
from langchain.chains.question_answering import load_qa_chain
from langchain.chains import LLMChain
from langchain.chains.conversational_retrieval.prompts import CONDENSE_QUESTION_PROMPT
import re
def get_embedding():
    return HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)
def generate_embedding(text):
    embedding_model = get_embedding()
    return embedding_model.embed_query(text)  # or embed_documents([text]) if needed

# FAISS_INDEX_PATH = "faiss_index"

def get_or_create_faiss_index(faiss_index_path):
    FAISS_INDEX_PATH = "vectorDB/"+faiss_index_path
    # print(FAISS_INDEX_PATH)
    embedding_model = get_embedding()

    if os.path.exists(FAISS_INDEX_PATH):
        # Load FAISS index if it exists
        vectorstore = FAISS.load_local(FAISS_INDEX_PATH, embedding_model, allow_dangerous_deserialization=True)
    else:
        # Create a new FAISS index if it doesn't exist
        from langchain_community.document_loaders import UnstructuredURLLoader
        from langchain.text_splitter import RecursiveCharacterTextSplitter
        
        # Sample URLs
        urls = [
            "https://google.github.io/styleguide/docguide/style.html",
            "https://www.markdownguide.org/basic-syntax/",
            "https://gist.github.com/rt2zz/e0a1d6ab2682d2c47746950b84c0b6ee",
            "https://gist.github.com/allysonsilva/85fff14a22bbdf55485be947566cc09e",
            "https://israelmitolu.hashnode.dev/markdown-for-technical-writers-tips-tricks-and-best-practices"
        ]
        # urls = [
        #     "https://thebarista.co.uk/blog/the-best-way-to-make-coffee-at-home",
        #     "https://food52.com/blog/26964-how-to-make-coffee?srsltid=AfmBOoqD6NA03WxwYtrfl_At3DsGM4tkuY-l6cqEERq5UW4FSBtHqBRb",
        #     "https://www.vegrecipesofindia.com/hot-coffee-recipe-cafe-style/",
        #     "https://www.yummytummyaarthi.com/how-to-make-perfect-cup-of-instant/"
        # ]
        loader = UnstructuredURLLoader(urls=urls)
        documents = loader.load()
        
        # Split text into chunks
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunked_texts = [chunk for doc in documents for chunk in text_splitter.split_text(doc.page_content)]
        
        # Create FAISS index and save it
        vectorstore = FAISS.from_texts(chunked_texts, embedding_model)
        vectorstore.save_local(FAISS_INDEX_PATH)
    
    return vectorstore

def get_llm():
    """Return a configured ChatGroq LLM instance."""
    return ChatGroq(
        model_name=LLM_MODEL_NAME,
        temperature=0.4,
        groq_api_key=GROQ_API_KEY
    )

def get_retrieval_chain(prompt_template, faiss_index_path = "faiss_index"):
    vectorstore = get_or_create_faiss_index(faiss_index_path)
    retriever = vectorstore.as_retriever()
    
    llm = get_llm()
    
    prompt_template = prompt_template
    # print(prompt_template)
    combine_docs_chain = load_qa_chain(llm, chain_type="stuff", prompt=prompt_template)
    question_generator = LLMChain(llm=llm, prompt=CONDENSE_QUESTION_PROMPT)

    # Define ConversationalRetrievalChain
    retrieval_qa_chain = ConversationalRetrievalChain(
        retriever=retriever,
        combine_docs_chain=combine_docs_chain,
        question_generator=question_generator,
        return_source_documents=True
    )
    
    return retrieval_qa_chain

def summarize_chat_history(chat_history, model="llama3-70b-8192"):
    """Summarize a conversation with code and markdown, focusing on key code snippets and relevant explanations."""
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are an AI that summarizes conversations involving code and markdown. "
                           "Extract only the key parts of the model's feedback and response, as well as the user's important markdown, code, hints, and problems. "
                           "This summary will be used as chat history for the next prompt, so it should focus on what's relevant and useful. "
                           "You should provide two summaries: one for the user's side, and one for the model's response."
            },
            {
                "role": "user",
                "content": f"Summarize the conversation (this will be used as chat history for the user's next prompt), extracting only the essential explanations and relevant content:\n\n{chat_history}"
            }
        ],
        model=model,
        temperature=0.3,  # Lower for consistency
        top_p=1,
        stop=None,
        stream=False,
    )
    return chat_completion.choices[0].message.content.strip()

def writter_summarize_chat_history(chat_history, model=LLM_MODEL_NAME):
    client = Groq(api_key=GROQ_API_KEY)
    """Summarize a conversation about reviewing and improving Markdown files, focusing on key insights, important user questions, and model suggestions."""
    
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an AI that summarizes conversations involving reviewing and improving Markdown files. "
                    "Your goal is to create a concise yet detailed summary that preserves important context for future conversations. "
                    "Ensure the summary includes:\n"
                    "- The model's suggestions for improvement.\n"
                    "- Any user questions that may be relevant for future queries.\n"
                    "- Any critical code or Markdown examples discussed.\n\n"
                    "Provide two structured summaries:\n"
                    "1. **User Input Summary**: Capture the user’s key questions, concerns, or Markdown-related issues.\n"
                    "2. **Model Response Summary**: Include the model’s key suggestions, explanations, and any important insights.\n\n"
                    "Keep the summary relevant, avoiding unnecessary details, but ensuring all useful information is retained."
                )
            },
            {
                "role": "user",
                "content": f"Summarize the conversation (this will be used as chat history for the next prompt), extracting only the essential insights, Markdown issues, and improvement suggestions:\n\n{chat_history}"
            }
        ],
        model=model,
        temperature=0.5,  # Ensures consistent and concise summaries
        top_p=1,
        stop=None,
        stream=False,
    )
    return chat_completion.choices[0].message.content.strip()

def developer_summarize_chat_history(chat_history, model=LLM_MODEL_NAME):
    client = Groq(api_key=GROQ_API_KEY)
    """Summarize a conversation about APIs, libraries, and product usage, focusing on key insights, implementation details, and troubleshooting steps."""
    
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an AI that summarizes conversations involving APIs, libraries, and product usage. "
                    "Your goal is to create a concise yet informative summary that preserves key context for future interactions. "
                    "Ensure the summary includes:\n"
                    "- The user's main questions or concerns regarding APIs, libraries, or products.\n"
                    "- The model’s explanations, suggestions, or troubleshooting steps.\n"
                    "- Any critical code snippets, configurations, or implementation details discussed.\n\n"
                    "Provide two structured summaries:\n"
                    "1. **User Input Summary**: Capture the user's key questions, challenges, or implementation goals.\n"
                    "2. **Model Response Summary**: Summarize the model’s key insights, explanations, and suggested solutions.\n\n"
                    "Keep the summary focused and relevant, ensuring all useful information is retained while avoiding unnecessary details."
                )
            },
            {
                "role": "user",
                "content": f"Summarize the conversation (this will be used as chat history for the next prompt), extracting only the essential insights, API/library/product-related questions, and troubleshooting guidance:\n\n{chat_history}"
            }
        ],
        model=model,
        temperature=0.5,  # Ensures consistent and concise summaries
        top_p=1,
        stop=None,
        stream=False,
    )
    return chat_completion.choices[0].message.content.strip()

def extract_markdown_sections(text):
    """
    Searches for Markdown between [[MARKDOWN_START]] and [[MARKDOWN_END]] tags.
    Returns a list of markdown sections.
    """
    pattern = r"\[\[MARKDOWN_START\]\](.*?)\[\[MARKDOWN_END\]\]"
    matches = re.findall(pattern, text, flags=re.DOTALL)
    if matches:
        print("Found")
        return matches
    else:
        print("Not Found")
        return ""


