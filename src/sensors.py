# src/sensors.py
from abc import ABC, abstractmethod
import random
from typing import List


class Sensor(ABC):
    """
    Abstract base class representing a generic sensor.
    """

    def __init__(self, id_: str):
        """
        Initialize the sensor with a unique identifier.

        Args:
            id_ (str): Unique identifier for the sensor.
        """
        self.id = id_

    @abstractmethod
    def read_data(self):
        """
        Read the current sensor data.

        Returns:
            Any: Sensor-specific data reading.
        """
        raise NotImplementedError

    @abstractmethod
    def detect_anomaly(self) -> bool:
        """
        Detect if the latest sensor reading is outside expected bounds.

        Returns:
            bool: True if anomaly detected, False otherwise.
        """
        raise NotImplementedError


class TemperatureSensor(Sensor):
    """
    Temperature sensor that tracks temperature readings and detects anomalies.
    """

    def __init__(self, id_: str, baseline: float = 22.0):
        """
        Initialize the temperature sensor with a baseline value.

        Args:
            id_ (str): Unique identifier for the sensor.
            baseline (float): Starting temperature in Celsius.
        """
        super().__init__(id_)
        self.history: List[float] = [baseline]

    def read_data(self) -> float:
        """
        Generate the next temperature reading by adding a small random variation.

        Returns:
            float: The new temperature reading.
        """
        next_val = round(self.history[-1] + random.uniform(-1.0, 1.0), 2)
        self.history.append(next_val)
        print(f"[TemperatureSensor] read {next_val}°C")
        return next_val

    def detect_anomaly(self, low: float = 18.0, high: float = 28.0) -> bool:
        """
        Check if the latest temperature reading is outside the given range.

        Args:
            low (float): Lower threshold for normal temperature.
            high (float): Upper threshold for normal temperature.

        Returns:
            bool: True if the temperature is abnormal, False otherwise.
        """
        latest = self.history[-1]
        is_anom = latest < low or latest > high
        if is_anom:
            print("[TemperatureSensor] anomaly detected")
        return is_anom

    def get_history(self) -> List[float]:
        """
        Get the history of all temperature readings.

        Returns:
            List[float]: List of recorded temperature readings.
        """
        return list(self.history)
