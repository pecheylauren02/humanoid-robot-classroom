# tests/test_delivery_task.py
import unittest
from src.tasks import DeliveryTask

class TestDeliveryTask(unittest.TestCase):

    def test_create_task_direct(self):
        task = DeliveryTask(id="1", item="Book", from_location="James", to_location="Miss Lauren")
        self.assertEqual(task.id, "1")
        self.assertEqual(task.item, "Book")
        self.assertEqual(task.from_location, "James")
        self.assertEqual(task.to_location, "Miss Lauren")
        self.assertEqual(task.status, "Pending")

    def test_create_task_factory(self):
        task = DeliveryTask.create("Pen", "Alice", "Bob")
        self.assertIsInstance(task.id, str)
        self.assertEqual(task.item, "Pen")
        self.assertEqual(task.from_location, "Alice")
        self.assertEqual(task.to_location, "Bob")
        self.assertEqual(task.status, "Pending")

    def test_mark_completed(self):
        task = DeliveryTask.create("Notebook", "Library", "Classroom")
        task.mark_completed()
        self.assertEqual(task.status, "Completed")

    def test_mark_failed(self):
        task = DeliveryTask.create("Eraser", "Office", "Desk")
        task.mark_failed()
        self.assertEqual(task.status, "Failed")

    def test_unique_ids_from_factory(self):
        task1 = DeliveryTask.create("Item1", "A", "B")
        task2 = DeliveryTask.create("Item2", "C", "D")
        self.assertNotEqual(task1.id, task2.id)
        self.assertNotEqual(task1.item, task2.item)  # sanity check

if __name__ == "__main__":
    unittest.main()
