# src/task_manager.py
from collections import deque
from typing import Deque, List, Optional
from .tasks import DeliveryTask


class TaskManager:
    def __init__(self, id_: str):
        self.id = id_
        self.task_queue: Deque[DeliveryTask] = deque()
        self.completed: List[str] = []

    def enqueue_task(self, task: DeliveryTask) -> None:
        self.task_queue.append(task)
        print(f"[TaskManager] enqueued {task.id}")

    def dequeue_task(self) -> Optional[DeliveryTask]:
        if self.task_queue:
            t = self.task_queue.popleft()
            print(f"[TaskManager] dequeued {t.id}")
            return t
        return None

    def mark_completed(self, task: DeliveryTask) -> None:
        task.mark_completed()
        self.completed.append(task.id)
        print(f"[TaskManager] marked completed {task.id}")

    def list_tasks(self) -> List[str]:
        return [t.id for t in list(self.task_queue)]
