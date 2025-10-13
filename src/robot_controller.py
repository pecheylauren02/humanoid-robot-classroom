from enum import Enum, auto
from .task_manager import TaskManager
from .sensors import TemperatureSensor
from .interaction import InteractionModule
from .tasks import DeliveryTask
import random
from typing import Dict, List, Tuple
from datetime import datetime

# List of objects the robot cannot deliver
FORBIDDEN_ITEMS = [
    "piano",
    "door",
    "desk",
    "chair",
    "fridge",
    "human",
    "dog",
    "cat",
    "animal",
    "mountain"
]

# Possible reasons for delivery failure
FAILURE_REASONS = [
    "path blocked by an obstacle",
    "destination is currently occupied",
    "battery level too low",
    "item slipped from my grip",
    "sensors temporarily malfunctioning",
    "door or passage closed",
    "object too heavy",
    "communication error",
    "unexpected obstacle detected",
    "internal system error"
]

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
        self.task_manager = TaskManager("TM1")
        self.sensor = TemperatureSensor("S1")
        self.interaction = InteractionModule("I1")
        self.history: List[Tuple] = []
        self.task_log: List[str] = []

    def change_state(self, new_state: RobotState) -> None:
        """Change the robot's state."""
        self.state = new_state

    def start(self) -> None:
        """Initialize the robot and display ready message."""
        self.change_state(RobotState.IDLE)
        print(self.interaction.display_message("Robot ready."))

    def deliver_material(self, item: str, from_location: str, to_location: str) -> str:
        """Check, enqueue, and execute a delivery task."""
        # Check for forbidden items
        if item.lower() in FORBIDDEN_ITEMS:
            message = f"My apologies, I cannot deliver '{item}' — it is too large, heavy, or unsafe for me to carry."
            self.task_log.append(f"{datetime.now()}: Rejected delivery of {item}")
            return message

        # Otherwise, create task normally
        task = DeliveryTask.create(item, from_location, to_location)
        self.task_manager.enqueue_task(task)
        return self.execute_task()

    def execute_task(self) -> str:
        """Execute the next task in the queue with random success/failure."""
        task = self.task_manager.dequeue_task()
        if not task:
            return "No tasks to execute."

        self.change_state(RobotState.EXECUTING)
        print(self.interaction.display_message(f"\nExecuting delivery {task.item} -> {task.to_location}"))

        # 85% chance success, 15% chance failure
        success = random.choices([True, False], weights=[0.85, 0.15])[0]

        if success:
            self.task_manager.mark_completed(task)
            self.history.append(("deliver", task.id))
            self.interaction.log_interaction("deliver", task.to_location)
            self.change_state(RobotState.COMPLETED)
            self.change_state(RobotState.IDLE)
            self.task_log.append(f"{datetime.now()}: Delivered {task.item} to {task.to_location}")
            return f"Delivered {task.item} to {task.to_location}"

        else:
            reason = random.choice(FAILURE_REASONS)
            task.mark_failed()
            self.history.append(("deliver_failed", task.id))
            self.interaction.log_interaction("deliver_failed", task.to_location)
            self.change_state(RobotState.ERROR)
            self.recover_from_error()
            self.task_log.append(f"{datetime.now()}: Failed to deliver {task.item} to {task.to_location} — {reason}")
            return (
                f"Delivery of {task.item} to {task.to_location} failed because {reason}. "
                "Please try again in a few minutes."
            )

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
            self.task_log.append(f"{datetime.now()}: Temperature anomaly detected: {temp}°C")
            return {"temperature": temp, "issue": True}

        self.interaction.log_interaction("temperature_ok", str(temp))
        self.task_log.append(f"{datetime.now()}: Temperature checked: {temp}°C")
        return {"temperature": temp, "issue": False}

    def greet_student(self, name: str) -> str:
        """Greet a student by name with added personalization and mood simulation."""
        self.change_state(RobotState.EXECUTING)

        # Add small randomization for variety and realism
        greetings = [
            f"Hello, {name}! Nice to see you today 😊",
            f"Good day, {name}! I hope you're ready to learn.",
            f"Hey {name}! You look ready for class 🚀",
            f"Greetings, {name}. Let’s make today productive!",
            f"Hi {name}! I’m glad you’re here."
        ]

        # Occasionally, the robot reacts to the classroom temperature
        current_temp = self.sensor.history[-1] if self.sensor.history else 22.0
        temp_comment = ""
        if current_temp < 19:
            temp_comment = " Brrr... it feels a bit chilly in here today ❄️"
        elif current_temp > 27:
            temp_comment = " Phew, it’s quite warm! I hope the fans are on ☀️"

        msg = random.choice(greetings) + temp_comment

        # Log everything
        self.interaction.log_interaction("greet", name)
        self.history.append(("greet", name))
        self.task_log.append(f"{datetime.now()}: Greeted student {name} (Temp: {current_temp}°C)")
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
