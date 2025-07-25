import unittest
import os
import sqlite3
from unittest.mock import patch
import db 


TEST_DB = "test_task_tracker.db"

def test_connection():
    database = sqlite3.connect(TEST_DB)
    database.row_factory = sqlite3.Row
    return database


patcher = patch("db.get_connection", new=test_connection)
patcher.start()
import task_service
patcher.stop()

class TestTaskService(unittest.TestCase):

    def setUp(self):
        self.database = test_connection()
        cursor = self.database.cursor()
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
        self.database.commit()
       

    def tearDown(self):
        self.database.close()
        if os.path.exists(TEST_DB):
            os.remove(TEST_DB)

    def test_add_and_get_task(self):
        task_service.add_task("Unit Test Task", "desc", "2025-07-23", False)
        tasks = task_service.get_all_tasks()
        self.assertEqual(len(tasks),1)
        self.assertEqual(tasks[0].title, "Unit Test Task")

    def test_update_task(self):
        task_service.add_task("Old Title", "desc", "2025-07-23", False)
        tasks = task_service.get_all_tasks()
        task_id = tasks[0].id

        task_service.update_task(task_id, "New Title", "Updated", "2025-07-23", True)
        updated_task = task_service.get_task_by_id(task_id)
        self.assertEqual(updated_task.title, "New Title")
        self.assertTrue(updated_task.completed)


    def test_delete_task(self):
        task_service.add_task("Temp Task", "desc", "2025-07-23", False)
        tasks = task_service.get_all_tasks()
        task_id = tasks[0].id

        task_service.delete_task(task_id)
        tasks_after = task_service.get_all_tasks()
        self.assertEqual(len(tasks_after), 0)

if __name__ == "__main__":
    unittest.main()
