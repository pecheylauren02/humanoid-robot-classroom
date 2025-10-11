# src/tasks.py
from dataclasses import dataclass
import uuid
from typing import Optional


@dataclass
class DeliveryTask:
    """
    Represents a delivery task for the humanoid robot, including item,
    source and destination locations, and status tracking.
    """
    id: str
    item: str
    from_location: str
    to_location: str
    status: str = "Pending"

    @classmethod
    def create(cls, item: str, from_location: str, to_location: str) -> "DeliveryTask":
        """
        Factory method to create a new DeliveryTask with a unique ID.

        Args:
            item (str): The item to be delivered.
            from_location (str): The starting location.
            to_location (str): The destination location.

        Returns:
            DeliveryTask: A new DeliveryTask instance with a unique ID.
        """
        return cls(id=str(uuid.uuid4()), item=item, from_location=from_location, to_location=to_location)

    def mark_completed(self) -> None:
        """
        Mark the delivery task as completed by updating its status.
        """
        self.status = "Completed"

    def mark_failed(self) -> None:
        """
        Mark the delivery task as failed by updating its status.
        """
        self.status = "Failed"
