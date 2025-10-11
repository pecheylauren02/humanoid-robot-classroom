# src/robot_controller.py
from enum import Enum, auto
from .task_manager import TaskManager
from .sensors import TemperatureSensor
from .interaction import InteractionModule
from .tasks import DeliveryTask
import random
from typing import Dict, List, Tuple


class RobotState(Enum):
    """Enumeration representing the various states of the humanoid robot."""
    IDLE = auto()
    EXECUTING = auto()
    COMPLETED = auto()
    ERROR = auto()
    RECOVERING = auto()


class RobotController:
    """Controller for managing humanoid robot operations."""

    def __init__(self, id_: str):
        """Initialize the robot controller."""
        self.id = id_
        self.state = RobotState.IDLE
        self.task_manager = TaskManager("TM1")      # Removed verbose
        self.sensor = TemperatureSensor("S1")
        self.interaction = InteractionModule("I1")  # Removed verbose
        self.history: List[Tuple] = []

    def change_state(self, new_state: RobotState) -> None:
        """Change the robot's state."""
        self.state = new_state

    def start(self) -> None:
        """Initialize the robot and display ready message."""
        self.change_state(RobotState.IDLE)
        print(self.interaction.display_message("Robot ready."))

    def deliver_material(self, item: str, from_location: str, to_location: str) -> str:
        """Enqueue a delivery task and execute it."""
        task = DeliveryTask.create(item, from_location, to_location)
        self.task_manager.enqueue_task(task)
        return self.execute_task()

    def execute_task(self) -> str:
        """Execute the next task in the queue."""
        task = self.task_manager.dequeue_task()
        if not task:
            return "No tasks to execute."

        self.change_state(RobotState.EXECUTING)
        print(self.interaction.display_message(f"Executing delivery {task.item} -> {task.to_location}"))

        # Simulate success/failure
        success = random.choices([True, False], weights=[0.85, 0.15])[0]
        if success:
            self.task_manager.mark_completed(task)
            self.history.append(("deliver", task.id))
            self.interaction.log_interaction("deliver", task.to_location)
            self.change_state(RobotState.COMPLETED)
            self.change_state(RobotState.IDLE)
            return f"Delivered {task.item} to {task.to_location}"
        else:
            task.mark_failed()
            self.history.append(("deliver_failed", task.id))
            self.interaction.log_interaction("deliver_failed", task.to_location)
            self.change_state(RobotState.ERROR)
            self.recover_from_error()
            return f"Delivery {task.item} to {task.to_location} failed"

    def recover_from_error(self) -> None:
        """Recover from an error state."""
        self.change_state(RobotState.RECOVERING)
        self.change_state(RobotState.IDLE)

    def monitor_environment(self) -> Dict:
        """Monitor environmental conditions."""
        temp = self.sensor.read_data()
        anomaly = self.sensor.detect_anomaly()
        self.history.append(("monitor", temp))
        if anomaly:
            self.interaction.log_interaction("temperature_anomaly", str(temp))
            return {"temperature": temp, "issue": True}
        self.interaction.log_interaction("temperature_ok", str(temp))
        return {"temperature": temp, "issue": False}

    def greet_student(self, name: str) -> str:
        """Greet a student by name."""
        self.change_state(RobotState.EXECUTING)
        msg = f"Hello, {name}!"
        print(self.interaction.display_message(msg))
        self.interaction.log_interaction("greet", name)
        self.history.append(("greet", name))
        self.change_state(RobotState.COMPLETED)
        self.change_state(RobotState.IDLE)
        return msg

    def get_status(self) -> Dict:
        """Get current robot status."""
        return {
            "id": self.id,
            "state": self.state.name,
            "history": list(self.history),
            "task_queue": self.task_manager.list_tasks(),
            "interaction_log": self.interaction.get_log(),
            "temperature_history": self.sensor.get_history()
        }
