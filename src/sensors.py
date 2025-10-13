from abc import ABC, abstractmethod
import random
from typing import List

# --- ANSI color codes ---
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
RESET = "\033[0m"


class Sensor(ABC):
    """Abstract base class representing a generic sensor."""

    def __init__(self, id_: str):
        self.id = id_

    @abstractmethod
    def read_data(self):
        """Simulate reading data from the sensor."""
        raise NotImplementedError

    @abstractmethod
    def detect_anomaly(self) -> bool:
        """Detect whether an abnormal condition has occurred."""
        raise NotImplementedError


class TemperatureSensor(Sensor):
    """Tracks temperature readings and detects anomalies."""

    def __init__(self, id_: str, baseline: float = 22.0):
        super().__init__(id_)
        self.temperature: float = baseline
        self.history: List[float] = [baseline]

    def read_data(self) -> float:
        """Simulate reading a new temperature value."""
        if random.random() < 0.1:
            extreme_change = random.choice([-5.0, 5.0, -7.0, 7.0])
            self.temperature = round(self.history[-1] + extreme_change, 2)
        else:
            self.temperature = round(
                self.history[-1] + random.uniform(-1.0, 1.0), 2
            )

        self.history.append(self.temperature)
        return self.temperature

    def detect_anomaly(self, low: float = 18.0, high: float = 28.0) -> bool:
        """Check if the latest temp reading is outside the safe range."""
        latest = self.history[-1]
        return latest < low or latest > high

    def get_history(self) -> List[float]:
        """Return the full temperature history."""
        return list(self.history)
