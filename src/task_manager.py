# src/task_manager.py
from collections import deque
from typing import Deque, List, Optional
from .tasks import DeliveryTask


class TaskManager:
    """
    Manager class for handling delivery tasks for the humanoid robot.
    Uses a queue for task scheduling and tracks completed tasks.
    """

    def __init__(self, id_: str):
        """
        Initialize the task manager with a unique identifier.

        Args:
            id_ (str): Unique identifier for the task manager.
        """
        self.id = id_
        self.task_queue: Deque[DeliveryTask] = deque()
        self.completed: List[str] = []

    def enqueue_task(self, task: DeliveryTask) -> None:
        """
        Add a delivery task to the queue.

        Args:
            task (DeliveryTask): Task to enqueue.
        """
        self.task_queue.append(task)
        # print(f"[TaskManager] enqueued {task.id}")

    def dequeue_task(self) -> Optional[DeliveryTask]:
        """
        Remove and return the next task from the queue.

        Returns:
            Optional[DeliveryTask]: The next task if available, otherwise None.
        """
        if self.task_queue:
            t = self.task_queue.popleft()
            # print(f"[TaskManager] dequeued {t.id}")
            return t
        return None

    def mark_completed(self, task: DeliveryTask) -> None:
        """
        Mark a task as completed and add it to the completed list.

        Args:
            task (DeliveryTask): Task to mark as completed.
        """
        task.mark_completed()
        self.completed.append(task.id)
        # print(f"[TaskManager] marked completed {task.id}")

    def list_tasks(self) -> List[str]:
        """
        List the IDs of all tasks currently in the queue.

        Returns:
            List[str]: List of task IDs in the queue.
        """
        return [t.id for t in list(self.task_queue)]
