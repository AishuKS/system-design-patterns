#structure
# Product - ParkingSpot (abstract class for parking spot)
# ConcreteProduct - CarSpot, BikeSpot, TruckSpot
# Creator - ParkingLot (abstract class with create_spot() method)
# ConcreteCreator - CarParkingLot, BikeParkingLot, TruckParkingLot

from abc import ABC, abstractmethod

#--------------------Product----------------------
class ParkingSpot(ABC):
    @abstractmethod
    def park(self, vehicle_number):
        pass

#------------------ConcreteProduct----------------
class CarSpot(ParkingSpot):
    def park(self, vehicle_number):
        print(f"Car {vehicle_number} parked in CarSpot")

class BikeSpot(ParkingSpot):
    def park(self, vehicle_number):
        print(f"Bike {vehicle_number} parked in BikeSpot")
    
class TruckSpot(ParkingSpot):
    def park(self, vehicle_number):
        print(f"Truck {vehicle_number} parked in TruckSpot")

#----------------------Creator---------------
class ParkingLot(ABC):
    @abstractmethod
    def create_spot(self):
        pass
    
    def allocate(self, vehicle_number):
        spot = self.create_spot()
        spot.park(vehicle_number)

class CarParkingLot(ParkingLot):
    def create_spot(self):
        return CarSpot()

car_lot = CarParkingLot()
car_lot.allocate("CAR-123")