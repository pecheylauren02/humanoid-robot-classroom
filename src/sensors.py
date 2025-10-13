from abc import ABC, abstractmethod
import random
from typing import List


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
    """Temperature sensor that tracks temperature readings and detects anomalies."""

    def __init__(self, id_: str, baseline: float = 22.0):
        super().__init__(id_)
        self.temperature: float = baseline
        self.history: List[float] = [baseline]

    def read_data(self) -> float:
        """Simulate reading a new temperature value."""
        # 10% chance of extreme high or low reading
        if random.random() < 0.1:
            extreme_change = random.choice([-5.0, 5.0, -7.0, 7.0])
            self.temperature = round(self.history[-1] + extreme_change, 2)
        else:
            self.temperature = round(self.history[-1] + random.uniform(-1.0, 1.0), 2)

        self.history.append(self.temperature)
        print(f"[Sensor] Current temperature: {self.temperature}°C")
        return self.temperature

    def detect_anomaly(self, low: float = 18.0, high: float = 28.0) -> bool:
        """Check if the latest temperature reading is outside the safe range."""
        latest = self.history[-1]
        if latest < low:
            print(f"[Warning] It's too cold! Current temperature: {latest}°C ❄️")
            print("Please close the windows or adjust the heating.")
            return True
        elif latest > high:
            print(f"\n[Warning] It's too hot! Current temperature: {latest}°C ☀️")
            print("Please turn on the air conditioner or open a window.")
            return True
        return False

    def get_history(self) -> List[float]:
        """Return the full temperature history."""
        return list(self.history)
