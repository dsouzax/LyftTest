from tires.tires import Tires
from utils import add_years_to_date


class OctoprimeTire(Tires):
    def __init__(self, wearArray):
        self.wearArray = wearArray


    def needs_service(self):
        if sum(self.wearArray) >= 3:
            return True
        return False