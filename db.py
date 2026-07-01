import sqlite3

def get_db():
    connect = sqlite3.connect("database.db")
    connect.row_factory = sqlite3.Row
    return connect

def create_user(username, password_hash):
    connect = get_db()
    cursor = connect.cursor()

    cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, password_hash))
    
    connect.commit()
    connect.close()

def get_user(username):
    connect = get_db()
    cursor = connect.cursor()

    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))

    user = cursor.fetchone()
    connect.close()

    return user
