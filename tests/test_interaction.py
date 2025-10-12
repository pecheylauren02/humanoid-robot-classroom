# tests/test_interaction_module.py
import unittest
from src.interaction import InteractionModule


class TestInteractionModule(unittest.TestCase):
    
    def setUp(self):
        self.module = InteractionModule("IM-001")

    def test_display_message(self):
        msg = self.module.display_message("Hello, Teacher!")
        self.assertEqual(msg, "Robot: Hello, Teacher!")

    def test_log_interaction(self):
        self.module.log_interaction("Delivered book", "Alice")
        log = self.module.get_log()
        self.assertEqual(len(log), 1)
        self.assertEqual(log[0], ("Delivered book", "Alice"))

    def test_undo_last(self):
        self.module.log_interaction("Delivered book", "Alice")
        undone = self.module.undo_last()
        self.assertEqual(undone, ("Delivered book", "Alice"))

        # The undo should add an "undo" entry to the log
        log = self.module.get_log()
        self.assertEqual(log[-1], ("undo", "Alice"))

    def test_undo_when_empty(self):
        result = self.module.undo_last()
        self.assertIsNone(result)

    def test_multiple_logs_and_undo(self):
        self.module.log_interaction("Delivered book", "Alice")
        self.module.log_interaction("Greeted student", "Bob")
        self.assertEqual(len(self.module.get_log()), 2)

        undone = self.module.undo_last()
        self.assertEqual(undone, ("Greeted student", "Bob"))

        log = self.module.get_log()
        # Last log entry should be the undo
        self.assertEqual(log[-1], ("undo", "Bob"))
        self.assertEqual(len(log), 3)  # original 2 actions + 1 undo

    def test_get_log_returns_copy(self):
        self.module.log_interaction("Delivered book", "Alice")
        log_copy = self.module.get_log()
        log_copy.append(("Fake action", None))
        # Original log should not be modified
        self.assertEqual(len(self.module.get_log()), 1)


if __name__ == "__main__":
    unittest.main()
