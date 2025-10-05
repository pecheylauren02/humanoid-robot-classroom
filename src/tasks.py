# src/tasks.py
from dataclasses import dataclass
import uuid
from typing import Optional

@dataclass
class DeliveryTask:
    id: str
    item: str
    from_location: str
    to_location: str
    status: str = "Pending"

    @classmethod
    def create(cls, item: str, from_location: str, to_location: str):
        return cls(id=str(uuid.uuid4()), item=item, from_location=from_location, to_location=to_location)

    def mark_completed(self):
        self.status = "Completed"

    def mark_failed(self):
        self.status = "Failed"
