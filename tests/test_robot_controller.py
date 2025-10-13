import unittest
from datetime import datetime
from src.robot_controller import RobotController, RobotState, FORBIDDEN_ITEMS

# Fake dependencies
class FakeTaskManager:
    def __init__(self, name):
        self.tasks = []
    def enqueue_task(self, task):
        self.tasks.append(task)
    def dequeue_task(self):
        return self.tasks.pop(0) if self.tasks else None
    def mark_completed(self, task):
        task.completed = True
    def list_tasks(self):
        return self.tasks

class FakeSensor:
    def __init__(self, name):
        self.history = [22.0]
    def read_data(self):
        return 22.0
    def detect_anomaly(self):
        return False
    def get_history(self):
        return self.history

class FakeInteraction:
    def __init__(self, name):
        self.log = []
    def display_message(self, msg):
        return msg
    def log_interaction(self, action, target):
        self.log.append((action, target))
    def get_log(self):
        return self.log

class FakeDeliveryTask:
    def __init__(self, item, from_loc, to_loc):
        self.item = item
        self.to_location = to_loc
        self.id = "task123"
        self.completed = False
    @staticmethod
    def create(item, from_loc, to_loc):
        return FakeDeliveryTask(item, from_loc, to_loc)
    def mark_failed(self):
        self.completed = False

# Test class
class TestRobotController(unittest.TestCase):
    def setUp(self):
        self.controller = RobotController("R1")
        # Replace dependencies with fakes
        self.controller.task_manager = FakeTaskManager("TM1")
        self.controller.sensor = FakeSensor("S1")
        self.controller.interaction = FakeInteraction("I1")
        self.controller.DeliveryTask = FakeDeliveryTask  # not used, deliver_material calls class method

    def test_initial_state(self):
        self.assertEqual(self.controller.state, RobotState.IDLE)

    def test_deliver_forbidden_item(self):
        msg = self.controller.deliver_material("piano", "A", "B")
        self.assertIn("cannot deliver", msg)

    def test_deliver_normal_item_success(self):
        # Patch random to force success
        import random
        original_choices = random.choices
        random.choices = lambda *a, **k: [True]

        msg = self.controller.deliver_material("book", "A", "B")
        self.assertIn("Delivered book", msg)
        self.assertEqual(self.controller.history[-1][0], "deliver")

        random.choices = original_choices

    def test_greet_student(self):
        import random
        original_choice = random.choice
        random.choice = lambda x: x[0]  # always pick first greeting

        msg = self.controller.greet_student("John")
        self.assertIn("Hello, John", msg)
        self.assertEqual(self.controller.history[-1], ("greet", "John"))

        random.choice = original_choice

    def test_monitor_environment(self):
        result = self.controller.monitor_environment()
        self.assertEqual(result, {"temperature": 22.0, "issue": False})

    def test_get_status_structure(self):
        status = self.controller.get_status()
        self.assertIsInstance(status["task_queue"], list)
        self.assertIsInstance(status["interaction_log"], list)
        self.assertIsInstance(status["temperature_history"], list)


if __name__ == "__main__":
    unittest.main()
