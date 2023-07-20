from model.VehicleBaseModel import Repair, Vehicle
from model.VehicleModel import Truck, Trailer

def addTruckDriver(truck: Truck, driver: Trailer):
    truck.truckDriver = driver

def addTrailer(truck: Truck, trailer: Trailer):
    truck.trailer = trailer
    addTruck(trailer, truck)

def addTruck(trailer: Trailer , truck: Truck):
    trailer.truck = truck

def addRepair(vehicle: Vehicle, date: str, description: str):
    vehicle.repairs.append(Repair(date, description, vehicle))

def showRepairs(vehicle: Vehicle):
    for repair in vehicle.repairs:
      print(repair)