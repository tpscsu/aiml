import unittest
from temperature_converter import celsius_to_fahrenheit, fahrenheit_to_celsius


class TestTemperatureConverter(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(0), 32)
        self.assertAlmostEqual(celsius_to_fahrenheit(100), 212)
        self.assertAlmostEqual(celsius_to_fahrenheit(-40), -40)
        self.assertAlmostEqual(celsius_to_fahrenheit(37), 98.6, places=1)

    def test_fahrenheit_to_celsius(self):
        # Test known values
        self.assertAlmostEqual(fahrenheit_to_celsius(32), 0)
        self.assertAlmostEqual(fahrenheit_to_celsius(212), 100)
        self.assertAlmostEqual(fahrenheit_to_celsius(-40), -40)
        self.assertAlmostEqual(fahrenheit_to_celsius(98.6), 37, places=1)

    def test_invalid_values(self):
        with self.assertRaises(TypeError):
            celsius_to_fahrenheit("invalid")
        with self.assertRaises(TypeError):
            fahrenheit_to_celsius("invalid")


if __name__ == "__main__":
    unittest.main()
