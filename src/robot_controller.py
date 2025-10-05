# src/robot_controller.py
from enum import Enum, auto
from .task_manager import TaskManager
from .sensors import TemperatureSensor
from .interaction import InteractionModule
from .tasks import DeliveryTask
import random
from typing import Dict


class RobotState(Enum):
    IDLE = auto()
    EXECUTING = auto()
    COMPLETED = auto()
    ERROR = auto()
    RECOVERING = auto()


class RobotController:
    def __init__(self, id_: str):
        self.id = id_
        self.state = RobotState.IDLE
        self.task_manager = TaskManager("TM1")
        self.sensor = TemperatureSensor("S1")
        self.interaction = InteractionModule("I1")
        self.history: list = []  # records tuples like ('deliver', taskid)

    def change_state(self, new_state: RobotState) -> None:
        print(f"[RobotController] {self.state.name} -> {new_state.name}")
        self.state = new_state

    def start(self) -> None:
        self.change_state(RobotState.IDLE)
        self.interaction.display_message("Robot ready.")

    def deliver_material(self, item: str, from_location: str, to_location: str) -> str:
        task = DeliveryTask.create(item, from_location, to_location)
        self.task_manager.enqueue_task(task)
        # attempt to execute immediately per your activity diagram
        return self.execute_task()

    def execute_task(self) -> str:
        task = self.task_manager.dequeue_task()
        if not task:
            return "No tasks."

        self.change_state(RobotState.EXECUTING)
        self.interaction.display_message(f"Executing delivery {task.item} -> {task.to_location}")

        # simulate success/failure
        success = random.choices([True, False], weights=[0.85, 0.15])[0]  # mostly succeed
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
            # simple recovery attempt
            self.recover_from_error()
            return f"Delivery {task.id} failed"

    def recover_from_error(self) -> None:
        print("[RobotController] attempting recovery")
        self.change_state(RobotState.RECOVERING)
        # simple recovery logic — could requeue
        self.change_state(RobotState.IDLE)

    def monitor_environment(self) -> Dict:
        temp = self.sensor.read_data()
        anomaly = self.sensor.detect_anomaly()
        self.history.append(("monitor", temp))
        if anomaly:
            self.interaction.log_interaction("temperature_anomaly", str(temp))
            return {"temperature": temp, "issue": True}
        self.interaction.log_interaction("temperature_ok", str(temp))
        return {"temperature": temp, "issue": False}

    def greet_student(self, name: str) -> str:
        self.change_state(RobotState.EXECUTING)
        msg = f"Hello, {name}!"
        self.interaction.display_message(msg)
        self.interaction.log_interaction("greet", name)
        self.history.append(("greet", name))
        self.change_state(RobotState.COMPLETED)
        self.change_state(RobotState.IDLE)
        return msg

    def get_status(self):
        return {
            "id": self.id,
            "state": self.state.name,
            "history": list(self.history),
            "task_queue": self.task_manager.list_tasks(),
            "interaction_log": self.interaction.get_log(),
            "temperature_history": self.sensor.get_history()
        }
