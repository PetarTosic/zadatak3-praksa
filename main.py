from model.UserModel import TruckDriver, Manager, Dispatcher
from model.VehicleModel import Truck, Trailer
from helpers.user_helpers import *
from helpers.vehicle_helpers import *

truck1 = Truck(10, 100000, 2010, 500)
truck2 = Truck(10, 150000, 2013, 600)

trailer1 = Trailer(4, 50000, 2021, 'container')
truck1.addRepair('15-02-2023', 'Fixed engine')
truck1.addTrailer(trailer1)

driver1 = TruckDriver('Marko', 'Markovic','21-02-1993', '281839401', '5 years', 40, 34)
driver2 = TruckDriver('Miomir', 'Markovic','21-02-1993', '281839401', '5 years', 40, 34)
driver3 = TruckDriver('Dragoljub', 'Dragic','21-02-1993', '281839401', '5 years', 40, 34)
addTruck(driver1, truck1)

manager1 = Manager('Petar', 'Petrovic','21-02-1993', '281839401', '5 years', 40, 34)
dispatcher1 = Dispatcher('Nikola', 'Nikolic','21-02-1993', '281839401', '5 years', 40, 34)

addTruck(driver2, truck2)
addTruckDriver(manager1, driver1)
addDispatcher(manager1, dispatcher1)
addTruckDriver(dispatcher1, driver1)

setArea(dispatcher1, 'Downtown')
giveDriverJob(dispatcher1, 'something', driver1)

addTruck(driver1, truck1)