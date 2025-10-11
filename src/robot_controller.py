# src/robot_controller.py
from enum import Enum, auto
from .task_manager import TaskManager
from .sensors import TemperatureSensor
from .interaction import InteractionModule
from .tasks import DeliveryTask
import random
from typing import Dict, List, Tuple


class RobotState(Enum):
    """
    Enumeration representing the various states of the humanoid robot.
    """
    IDLE = auto()
    EXECUTING = auto()
    COMPLETED = auto()
    ERROR = auto()
    RECOVERING = auto()


class RobotController:
    """
    Controller class for managing the operations of a humanoid robot, 
    including task execution, environmental monitoring, and interactions.
    """

    def __init__(self, id_: str):
        """
        Initialize the robot controller.

        Args:
            id_ (str): Unique identifier for the robot.
        """
        self.id = id_
        self.state = RobotState.IDLE
        self.task_manager = TaskManager("TM1")
        self.sensor = TemperatureSensor("S1")
        self.interaction = InteractionModule("I1")
        self.history: List[Tuple] = []  # records tuples like ('deliver', taskid)

    def change_state(self, new_state: RobotState) -> None:
        """
        Change the robot's state and print a log message.

        Args:
            new_state (RobotState): The new state to transition to.
        """
        print(f"[RobotController] {self.state.name} -> {new_state.name}")
        self.state = new_state

    def start(self) -> None:
        """
        Initialize the robot and display a ready message.
        """
        self.change_state(RobotState.IDLE)
        self.interaction.display_message("Robot ready.")

    def deliver_material(self, item: str, from_location: str, to_location: str) -> str:
        """
        Enqueue a delivery task and execute it immediately.

        Args:
            item (str): The item to be delivered.
            from_location (str): The starting location of the item.
            to_location (str): The destination location for delivery.

        Returns:
            str: Result of the task execution.
        """
        task = DeliveryTask.create(item, from_location, to_location)
        self.task_manager.enqueue_task(task)
        return self.execute_task()

    def execute_task(self) -> str:
        """
        Execute the next task in the queue, simulating possible success or failure.

        Returns:
            str: Message indicating the outcome of the task.
        """
        task = self.task_manager.dequeue_task()
        if not task:
            return "No tasks."

        self.change_state(RobotState.EXECUTING)
        self.interaction.display_message(f"Executing delivery {task.item} -> {task.to_location}")

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
            return f"Delivery {task.id} failed"

    def recover_from_error(self) -> None:
        """
        Attempt to recover from an error state and return the robot to idle.
        """
        print("[RobotController] attempting recovery")
        self.change_state(RobotState.RECOVERING)
        # Simple recovery logic — could requeue task or notify
        self.change_state(RobotState.IDLE)

    def monitor_environment(self) -> Dict:
        """
        Monitor environmental conditions via sensors.

        Returns:
            Dict: Dictionary containing temperature data and anomaly status.
        """
        temp = self.sensor.read_data()
        anomaly = self.sensor.detect_anomaly()
        self.history.append(("monitor", temp))
        if anomaly:
            self.interaction.log_interaction("temperature_anomaly", str(temp))
            return {"temperature": temp, "issue": True}
        self.interaction.log_interaction("temperature_ok", str(temp))
        return {"temperature": temp, "issue": False}

    def greet_student(self, name: str) -> str:
        """
        Greet a student by name and log the interaction.

        Args:
            name (str): Name of the student.

        Returns:
            str: Greeting message.
        """
        self.change_state(RobotState.EXECUTING)
        msg = f"Hello, {name}!"
        self.interaction.display_message(msg)
        self.interaction.log_interaction("greet", name)
        self.history.append(("greet", name))
        self.change_state(RobotState.COMPLETED)
        self.change_state(RobotState.IDLE)
        return msg

    def get_status(self) -> Dict:
        """
        Get the current status of the robot, including task queue, history, and logs.

        Returns:
            Dict: Current status of the robot.
        """
        return {
            "id": self.id,
            "state": self.state.name,
            "history": list(self.history),
            "task_queue": self.task_manager.list_tasks(),
            "interaction_log": self.interaction.get_log(),
            "temperature_history": self.sensor.get_history()
        }
