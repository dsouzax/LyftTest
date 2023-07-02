from tires.tires import Tires


class CarriganTire(Tires):
    def __init__(self, wearArray):
        self.wearArray = wearArray


    def needs_service(self):
        for wearArray in self.wearArray:
            if wearArray >= 0.9:
                return True
        return False
        