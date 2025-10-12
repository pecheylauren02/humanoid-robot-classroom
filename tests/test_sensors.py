# tests/test_sensors.py
import unittest
from src.sensors import Sensor, TemperatureSensor
from abc import ABC
import random

class TestTemperatureSensor(unittest.TestCase):

    def setUp(self):
        # Seed random for deterministic tests
        random.seed(0)
        self.sensor = TemperatureSensor("T-001", baseline=22.0)

    def test_initial_history(self):
        # The baseline value should be in history
        self.assertEqual(self.sensor.history, [22.0])

    def test_read_data_appends_to_history(self):
        val1 = self.sensor.read_data()
        val2 = self.sensor.read_data()
        self.assertEqual(len(self.sensor.history), 3)  # baseline + 2 reads
        self.assertEqual(self.sensor.history[-2], val1)
        self.assertEqual(self.sensor.history[-1], val2)

    def test_detect_anomaly_returns_false_for_normal_range(self):
        # Generate values within range
        for _ in range(5):
            self.sensor.read_data()
        self.assertFalse(self.sensor.detect_anomaly(low=18.0, high=28.0))

    def test_detect_anomaly_returns_true_for_out_of_range(self):
        # Force an out-of-range value
        self.sensor.history.append(30.0)
        self.assertTrue(self.sensor.detect_anomaly(low=18.0, high=28.0))
        self.sensor.history.append(15.0)
        self.assertTrue(self.sensor.detect_anomaly(low=18.0, high=28.0))

    def test_get_history_returns_copy(self):
        hist_copy = self.sensor.get_history()
        hist_copy.append(100.0)
        # Original history should not be affected
        self.assertNotEqual(self.sensor.history, hist_copy)

class TestSensorABC(unittest.TestCase):

    def test_cannot_instantiate_sensor(self):
        with self.assertRaises(TypeError):
            Sensor("S-001")  # Abstract class, cannot instantiate

    def test_abstract_methods_require_implementation(self):
        class DummySensor(Sensor):
            def read_data(self):
                return 0
            def detect_anomaly(self):
                return False

        dummy = DummySensor("D-001")
        self.assertEqual(dummy.read_data(), 0)
        self.assertFalse(dummy.detect_anomaly())

if __name__ == "__main__":
    unittest.main()
