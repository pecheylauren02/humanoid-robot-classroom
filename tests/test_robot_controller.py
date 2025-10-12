# tests/test_robot_controller.py
import unittest
from unittest.mock import MagicMock, patch
from src.robot_controller import RobotController, RobotState

class TestRobotController(unittest.TestCase):

    def setUp(self):
        # Patch dependencies to isolate RobotController
        with patch("src.robot_controller.TaskManager") as MockTaskManager, \
             patch("src.robot_controller.TemperatureSensor") as MockSensor, \
             patch("src.robot_controller.InteractionModule") as MockInteraction, \
             patch("src.robot_controller.DeliveryTask") as MockDeliveryTask:

            self.mock_task_manager = MockTaskManager.return_value
            self.mock_sensor = MockSensor.return_value
            self.mock_interaction = MockInteraction.return_value
            self.mock_task = MockDeliveryTask.create.return_value

            # Mock methods used in RobotController
            self.mock_task_manager.dequeue_task.return_value = self.mock_task
            self.mock_task.id = "task123"
            self.mock_task.item = "Book"
            self.mock_task.to_location = "Student Desk"
            self.mock_sensor.read_data.return_value = 25.0
            self.mock_sensor.detect_anomaly.return_value = False
            self.mock_interaction.display_message.return_value = "Message displayed"
            self.mock_interaction.get_log.return_value = []
            self.mock_sensor.get_history.return_value = []

            # Create controller
            self.robot = RobotController("R-001")
            self.robot.task_manager = self.mock_task_manager
            self.robot.sensor = self.mock_sensor
            self.robot.interaction = self.mock_interaction

    def test_start_sets_idle(self):
        self.robot.start()
        self.assertEqual(self.robot.state, RobotState.IDLE)

    def test_change_state(self):
        self.robot.change_state(RobotState.EXECUTING)
        self.assertEqual(self.robot.state, RobotState.EXECUTING)

    def test_deliver_material_success_logs_task(self):
        # Force success
        with patch("src.robot_controller.random.choices", return_value=[True]):
            self.robot.deliver_material("Book", "Library", "Student Desk")
        # Check log entry
        self.assertTrue(any("Delivered" in entry for entry in self.robot.task_log))

    def test_deliver_material_failure_logs_task(self):
        # Force failure
        with patch("src.robot_controller.random.choices", return_value=[False]):
            self.robot.deliver_material("Book", "Library", "Student Desk")
        self.assertTrue(any("Failed to deliver" in entry for entry in self.robot.task_log))

    def test_monitor_environment_logs_check(self):
        self.robot.monitor_environment()
        self.assertTrue(any("Temperature checked" in entry for entry in self.robot.task_log))

    def test_monitor_environment_anomaly_logs(self):
        self.mock_sensor.detect_anomaly.return_value = True
        self.robot.monitor_environment()
        self.assertTrue(any("Temperature anomaly detected" in entry for entry in self.robot.task_log))

    def test_greet_student_logs_task(self):
        greeting = self.robot.greet_student("Alice")
        self.assertEqual(greeting, "Hello, Alice!")
        self.assertTrue(any("Greeted student Alice" in entry for entry in self.robot.task_log))

    def test_get_status_returns_correct_keys(self):
        status = self.robot.get_status()
        keys = ["id", "state", "history", "task_queue", "interaction_log", "temperature_history"]
        for key in keys:
            self.assertIn(key, status)

if __name__ == "__main__":
    unittest.main()
