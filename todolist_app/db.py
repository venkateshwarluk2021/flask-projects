import sqlite3

def get_connection():
    database = sqlite3.connect("task_tracker.db")
    database.row_factory = sqlite3.Row
    return database

def init_db():
    database = get_connection()
    cursor = database.cursor()
    cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL,
description TEXT,
deadline TEXT,
completed INTEGER DEFAULT 0
)
""")
    database.commit()
    database.close()
