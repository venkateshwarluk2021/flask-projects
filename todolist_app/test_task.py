import unittest
from task import Task

class TestTaskModel(unittest.TestCase):

    def setUp(self):
        self.task = Task(1, "Test Task", "Just a test", "2025-07-23", False)

    def test_initial_state(self):
        self.assertEqual(self.task.id, 1)
        self.assertEqual(self.task.title, "Test Task")
        self.assertFalse(self.task.completed)

    def test_mark_completed(self):
        self.task.mark_completed()
        self.assertTrue(self.task.completed)

    def test_to_dict(self):
        task_dict = self.task.to_dict()
        self.assertEqual(task_dict["title"], "Test Task")
        self.assertEqual(task_dict["completed"], False)


if __name__ == "__main__":
    unittest.main()
