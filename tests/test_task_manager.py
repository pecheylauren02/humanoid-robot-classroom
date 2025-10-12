# tests/test_task_manager.py
import unittest
from collections import deque
from src.task_manager import TaskManager
from src.tasks import DeliveryTask

class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.manager = TaskManager("TM-001")
        # Use actual DeliveryTask.create() to get valid tasks with unique IDs
        self.task1 = DeliveryTask.create("Book", "James", "Miss Lauren")
        self.task2 = DeliveryTask.create("Pen", "Alice", "Bob")

    def test_enqueue_task(self):
        self.manager.enqueue_task(self.task1)
        self.assertEqual(self.manager.task_queue[0], self.task1)

    def test_dequeue_task(self):
        self.manager.enqueue_task(self.task1)
        self.manager.enqueue_task(self.task2)
        t = self.manager.dequeue_task()
        self.assertEqual(t, self.task1)
        self.assertEqual(list(self.manager.task_queue), [self.task2])

    def test_dequeue_empty_queue(self):
        t = self.manager.dequeue_task()
        self.assertIsNone(t)

    def test_mark_completed(self):
        self.manager.enqueue_task(self.task1)
        self.manager.mark_completed(self.task1)
        self.assertEqual(self.task1.status, "Completed")
        self.assertIn(self.task1.id, self.manager.completed)

    def test_list_tasks(self):
        self.manager.enqueue_task(self.task1)
        self.manager.enqueue_task(self.task2)
        task_ids = self.manager.list_tasks()
        self.assertEqual(task_ids, [self.task1.id, self.task2.id])

    def test_list_tasks_after_dequeue(self):
        self.manager.enqueue_task(self.task1)
        self.manager.enqueue_task(self.task2)
        self.manager.dequeue_task()
        task_ids = self.manager.list_tasks()
        self.assertEqual(task_ids, [self.task2.id])

if __name__ == "__main__":
    unittest.main()
