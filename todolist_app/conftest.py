import pytest
import sqlite3
import os
from unittest.mock import patch
import db
import task_service

TEST_DB = "test_task_tacker.db"

def get_test_connection():
    database = sqlite3.connect(TEST_DB)
    database.row_factory = sqlite3.Row
    return database

@pytest.fixture(scope="function")
def db_setup(monkeypatch):
    monkeypatch.setattr(db, "get_connection", get_test_connection)
    monkeypatch.setattr(task_service, "get_connection", get_test_connection)
    database = get_test_connection()
    cursor = database.cursor()
    cursor.execute("DROP TABLE IF EXISTS tasks")
    cursor.execute("""
CREATE TABLE tasks(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT,
description TEXT,
deadline TEXT,
completed INTEGER
)
""")
    
    database.commit()
    yield database
    database.close()


    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)
