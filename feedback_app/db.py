import sqlite3

def get_connection():
    database = sqlite3.connect("feedback.db")
    database.row_factory = sqlite3.Row
    return database
