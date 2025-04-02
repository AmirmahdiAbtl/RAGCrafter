import sqlite3

def init_db():
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()

        # MARKDOWNASSISTANT TABLES
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS chat_markdownassistant (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                language_model TEXT NOT NULL,
                start_chat TEXT NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS chat_detail_markdownassistant (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                chat_id INTEGER NOT NULL,
                prompt TEXT NOT NULL,
                api_spec_content TEXT DEFAULT '',  -- Stores OpenAPI file content if provided
                chat_response TEXT NOT NULL,
                time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                embedding BLOB NOT NULL,
                FOREIGN KEY (chat_id) REFERENCES chat_markdownassistant(id)
            )
        ''')

        # WRITTERASSISTANT TABLES
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS chat_writterassistant (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                summary TEXT,
                last_markdown TEXT,
                language_model TEXT NOT NULL,
                start_chat TEXT NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS chat_detail_writterassistant (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                chat_id INTEGER NOT NULL,
                prompt TEXT NOT NULL,
                code_files_content TEXT DEFAULT '',   -- Stores combined code files content if provided
                api_spec_content TEXT DEFAULT '',     -- Stores combined OpenAPI specs if provided
                chat_response TEXT NOT NULL,
                summary TEXT,
                markdown_content TEXT,
                time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (chat_id) REFERENCES chat_writterassistant(id)
            )
        ''')

        # DEVELOPERASSISTANT TABLES
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS chat_developerassistant (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                summary TEXT,
                pending_text TEXT,
                language_model TEXT NOT NULL,
                start_chat TEXT NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS chat_detail_developerassistant (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                chat_id INTEGER NOT NULL,
                prompt TEXT NOT NULL,
                chat_response TEXT NOT NULL,
                time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (chat_id) REFERENCES chat_developerassistant(id)
            )
        ''')

        conn.commit()