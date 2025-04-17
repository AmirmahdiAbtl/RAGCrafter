# RAG Crafter: Advanced RAG Application Builder

RAG Crafter is a comprehensive web application designed to create, manage, and interact with Retrieval-Augmented Generation (RAG) systems. It provides a user-friendly interface for building custom RAG applications with various language models and configurations.

## 🚀 Project Overview

RAG Crafter is built with Flask and provides a complete ecosystem for:
- Creating and managing RAG applications
- Configuring language models and embedding settings
- Building and maintaining vector databases
- Interactive chat interfaces for RAG systems
- Real-time monitoring of RAG application status

## 🛠️ Technical Architecture

### Backend Components
- **Flask Web Framework**: Powers the web application and API endpoints
- **SQLite Database**: Stores RAG configurations, chat histories, and user data
- **LangChain Integration**: Handles RAG pipeline construction and execution
- **ChromaDB**: Manages vector storage for document embeddings
- **FAISS**: Provides efficient similarity search capabilities
- **Sentence Transformers**: Generates document embeddings

### Frontend Components
- **HTML/CSS/JavaScript**: Modern, responsive user interface
- **Dark/Light Mode**: Theme customization for user comfort
- **Real-time Updates**: Dynamic status monitoring and chat interface
- **Interactive UI**: User-friendly controls for RAG management

## 📋 Core Features

### 1. RAG Creation and Management
- **Customizable Parameters**:
  - Language model selection (OpenAI, etc.)
  - Embedding model configuration
  - Chunk size and overlap settings
  - Vector database settings
- **Status Monitoring**:
  - Real-time progress tracking
  - Error handling and reporting
  - Resource utilization monitoring

### 2. Chat Interface
- **Interactive Communication**:
  - Real-time message exchange
  - Chat history management
  - Multiple chat sessions
- **Features**:
  - Message threading
  - Context preservation
  - Error handling
  - Loading states

### 3. Document Processing
- **Upload and Processing**:
  - Multiple document format support
  - Automatic chunking
  - Embedding generation
  - Vector storage
- **Management**:
  - Document versioning
  - Update handling
  - Storage optimization

### 4. System Configuration
- **Environment Setup**:
  - API key management
  - Model configuration
  - System parameters
- **Customization**:
  - UI themes
  - Chat settings
  - Performance tuning

## 🏗️ Project Structure

```
RAG-Crafter/
├── app.py           
├── database.py         
├── requirements.txt      
├── static/               
│   ├── css/             
│   │   ├── styles.css   
│   │   └── dark-theme.css
│   ├── js/              
│   │   ├── main.js      
│   │   ├── scriptchat.js 
│   │   └── theme.js     
│   └── img/        
└── templates/           
    ├── index.html     
    ├── panel.html     
    └── developerassistant.html 
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- SQL (included with Python)
- OpenAI API key (for language model access) / Ollama Model / Groq Api key

### Installation

1. Clone the repository:
```bash
git clone https://github.com/AmirmahdiAbtl/RAGCrafter/
cd RAG-Crafter
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```


### Running the Application

1. Start the Flask server:
```bash
python app.py

## But its better to use this command because of auto reloading
flask run --no-reload
```

2. Access the application:
Open your browser and navigate to `http://localhost:5000`

## 💻 Usage Guide

### Creating a New RAG Application

1. Navigate to the main dashboard
2. Click "Create New RAG"
3. Configure your RAG settings:
   - Select language model
   - Choose embedding model
   - Set chunk size and overlap
   - Configure vector database
4. Upload your documents
5. Suggest you the best prompts you need
6. Congradulate you can now start talking with your RAG model

### Using the Chat Interface

1. Select an existing RAG from the panel
2. Start a new chat or continue an existing one
3. Type your message and press Enter
4. View the RAG's response
5. Manage chat history and settings

### Managing Documents

1. Access the document management section
2. Upload new documents
3. View existing documents
4. Update or remove documents
5. Monitor processing status

## 🔧 Configuration


### Custom Settings
- Model parameters
- Embedding configurations
- UI preferences
- Chat settings

## 🐛 Troubleshooting

### Common Issues

1. **API Key Errors**
   - Verify your OpenAI API key
   - Check environment variables
   - Ensure proper key format

2. **Document Processing Issues**
   - Check file formats
   - Verify file sizes
   - Monitor system resources

3. **Chat Interface Problems**
   - Clear browser cache
   - Check network connectivity
   - Verify backend status

### Debugging

1. Enable debug mode in Flask
2. Check application logs
3. Monitor system resources
4. Verify database connections

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📞 Support

For support, please:
1. Check the documentation
2. Search existing issues
3. Create a new issue if needed
4. Contact the maintainers

## 🙏 Acknowledgments

- OpenAI for their language models
- LangChain team for their framework
- ChromaDB and FAISS teams
- All contributors and users
