from model.VehicleBaseModel import Repair

def addTruckDriver(truck: dict, driver: dict):
    truck.truckDriver = driver

def addTrailer(truck: dict, trailer: dict):
    truck.trailer = trailer
    addTruck(trailer, truck)

def addTruck(trailer: dict , truck: dict):
    trailer.truck = truck

def addRepair(vehicle: dict, date: str, description: str):
    vehicle.repairs.append(Repair(date, description, vehicle))

def showRepairs(vehicle: dict):
    for repair in vehicle.repairs:
      print(repair)