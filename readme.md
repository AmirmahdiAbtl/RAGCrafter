# RAG Crafter

RAG Crafter is a powerful tool for creating and managing Retrieval-Augmented Generation (RAG) applications. It provides an intuitive interface for building, customizing, and interacting with RAG models.

## Features

- **RAG Creation**: Create new RAG applications with customizable parameters
- **Chat Interface**: Interactive chat interface for communicating with your RAG models
- **Multiple Model Support**: Choose from various language models for your RAG applications
- **Dark/Light Mode**: Toggle between dark and light themes for comfortable usage
- **Project Management**: Organize and manage multiple RAG projects in one place
- **Real-time Status Updates**: Monitor the status of your RAG applications

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- SQLite (included with Python)

## Installation

1. Clone the repository:
```bash
git clone [your-repository-url]
cd RAG-Crafter
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Create a new RAG application:
   - Click on "Create New RAG" in the panel
   - Fill in the required information
   - Configure your RAG settings
   - Start using your RAG application

4. Chat with your RAG:
   - Select an existing RAG from the panel
   - Use the chat interface to interact with your RAG model
   - View chat history and manage conversations

## Project Structure

```
RAG-Crafter/
├── app.py                 # Main application entry point
├── database.py            # Database operations
├── requirements.txt       # Project dependencies
├── static/                # Static files
│   ├── css/              # CSS stylesheets
│   ├── js/               # JavaScript files
│   └── img/              # Images and icons
└── templates/            # HTML templates
    ├── index.html        # Landing page
    ├── panel.html        # Main dashboard
    └── developerassistant.html  # Chat interface
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

If you encounter any issues or have questions, please open an issue in the repository.

## Acknowledgments

- Thanks to all contributors who have helped improve this project
- Special thanks to the open-source community for their valuable tools and libraries
