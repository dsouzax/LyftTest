from tires.tires import Tires
from utils import add_years_to_date


class CarriganTire(Tires):
    def __init__(self, wearArray):
        self.wearArray = wearArray


    def needs_service(self):
        for wear_value in self.wear_values:
            if wear_value >= 0.9:
                return True
        return False
        