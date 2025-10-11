from abc import ABC, abstractmethod
import random
from typing import List


class Sensor(ABC):
    """Abstract base class representing a generic sensor."""

    def __init__(self, id_: str):
        self.id = id_

    @abstractmethod
    def read_data(self):
        raise NotImplementedError

    @abstractmethod
    def detect_anomaly(self) -> bool:
        raise NotImplementedError


class TemperatureSensor(Sensor):
    """Temperature sensor that tracks temperature readings and detects anomalies."""

    def __init__(self, id_: str, baseline: float = 22.0):
        super().__init__(id_)
        self.history: List[float] = [baseline]

    def read_data(self) -> float:
        next_val = round(self.history[-1] + random.uniform(-1.0, 1.0), 2)
        self.history.append(next_val)
        return next_val

    def detect_anomaly(self, low: float = 18.0, high: float = 28.0) -> bool:
        """Check if the latest temperature reading is outside the given range."""
        latest = self.history[-1]
        return latest < low or latest > high

    def get_history(self) -> List[float]:
        return list(self.history)
