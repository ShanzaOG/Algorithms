# A parking system to tell if there's available spaces for a car in a parking lot

class ParkingSystem:
    def __init__(self, small: int, medium: int, big: int):
        """

        :param small: int
        :param medium: int
        :param big: int
        """
        # initialize an array spots_available with an extra index for convenience
        self.spots_available = [0, small, medium, big]

    def addCar(self, carType: int) -> bool:
        """

        :param carType: Integer
        :return: Boolean
        """
        if self.spots_available[carType] == 0:
            return False
        self.spots_available[carType] -= 1
        return True


if __name__ == '__main__':
    obj = ParkingSystem(1, 2, 3)
    print(obj.addCar(1))
    print(obj.addCar(2))
    print(obj.addCar(2))
    print(obj.addCar(1))
