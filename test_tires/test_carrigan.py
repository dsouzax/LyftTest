import unittest

from tires.carrigan import CarriganTire


class TestCarriganTire(unittest.TestCase):
    def test_needs_service_true(self):
        carrigan_tire = CarriganTire([0.8, 0.4, 0.8, 0.9])
        self.assertTrue(carrigan_tire.needs_service())

    def test_needs_service_false(self):
        carrigan_tire = CarriganTire([0.8, 0.2, 0.6, 0.4])
        self.assertFalse(carrigan_tire.needs_service())