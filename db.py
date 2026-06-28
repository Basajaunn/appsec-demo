import sqlite3

def get_db():
    return sqlite3.connect("database.db")

def create_user(username, password_hash):
    connect = get_db()
    cursor = connect.cursor()
    cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, password_hash))
    connect.commit()
    connect.close()

