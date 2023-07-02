import unittest

from tires.octoprime import OctoprimeTire


class TestOctoprimeTire(unittest.TestCase):
    def test_needs_service_true(self):
        octoprime_tire = OctoprimeTire([0.8, 0.8, 0.9, 0.7])
        self.assertTrue(OctoprimeTire.needs_service())

    def test_needs_service_false(self):
        octoprime_tire = OctoprimeTire([0.3, 0.5, 0.8, 0.4])
        self.assertFalse(OctoprimeTire.needs_service())