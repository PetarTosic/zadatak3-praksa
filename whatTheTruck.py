from pydantic import BaseModel, Field
from typing import Union, List
from UserBaseModel import User
from VehicleBaseModel import Vehicle


class TruckDriver(User):
  manager_jmbg: Union[str, None] = Field(
    default=None,
    description="Truck drivers Manager"
  )
  dispatcher: Union[dict, None]
  truck = {}
  area: Union[str, None] = Field(
    default=None,
    description="The area where the driver works"
  )

  def __init__(self, first_name, last_name, birthday, jmbg, age, exp, workHours, pay):
    super().__init__(first_name, last_name, birthday, jmbg, age, exp, workHours)
    self.payPerMile = pay

  def addManager(self, mng):
    self.manager = mng

  def addDispatcher(self, disp):
    self.dispatcher = disp

  def addTruck(self, truck):
    self.truck = truck
    truck.addTruckDriver(self)

  def addLoadAndArea(self, load, area):
    if self.truck != {} and self.truck.trailer != {}:
      self.load = load
      self.area = area
    else:
      print('Driver doesn\'t have truck and/or trailer.')


class Dispatcher(User):
  manager = {}
  truckDrivers = []

  def __init__(self, first_name, last_name, birthday, jmbg, age, exp, workHours, pay):
    super().__init__(first_name, last_name, birthday, jmbg, age, exp, workHours)
    self.payPerMonth = pay

  def addManager(self, mng):
    self.manager = mng

  def addTruckDriver(self, driver):
    self.truckDrivers.append(driver)
    driver.addDispatcher(self)

  def setArea(self, area):
    self.area = area

  def giveDriverJob(self, load, driver):
    if driver not in self.truckDrivers:
      self.truckDrivers.append(driver)
    driver.addLoadAndArea(load, self.area)

  def showTruckDrivers(self):
    if self.truckDrivers != []:
      for driver in self.truckDrivers:
        print(driver)
    else:
      print('No drivers assigned.')


class Manager(User):
  truckDrivers: List[Union[TruckDriver, None]] = Field(
    default=None,
    description="Truck drivers that the manager manages."
  )

  truckDrivers = []

  dispatchers = []
  area = ""

  def __init__(self, first_name, last_name, birthday, jmbg, age, exp, workHours, pay):
    super().__init__(first_name, last_name, birthday, jmbg, age, exp, workHours)
    self.payPerMonth = pay

  def addTruckDriver(self, driver):
    self.truckDrivers.append(driver)
    driver.addManager(self.jmbg)
  
  def addDispatcher(self, disp):
    self.dispatchers.append(disp)
    disp.addManager(self)
    if self.area != "":
      disp.setArea(self.area)

  def setWorkingAre(self, area):
    self.area = area
    for disp in self.dispatchers:
      disp.setArea(area)

  def showDrivers(self):
    for driver in self.truckDrivers:
      print(driver)


class Truck(Vehicle):
  truckDriver = {}
  trailer = {}

  def __init__(self, wheels, miles, year, horsepower):
    super().__init__(wheels, miles, year)
    self.horsepower = horsepower
  
  def addTruckDriver(self, driver):
    self.truckDriver = driver

  def addTrailer(self, trailer):
    self.trailer = trailer
    trailer.addTruck = self

  def __str__(self):
    return "{} Truck with: {} wheels and {} miles".format(self.year, self.wheels, self.miles)


class Trailer(Vehicle):
  truck = {}

  def __init__(self, wheels, miles, year, type):
    super().__init__(wheels, miles, year)
    self.type = type

  def addTruck(self, truck):
    self.truck = truck

  def __str__(self):
    return "{} Trailer with: {} wheels and {} miles".format(self.year, self.wheels, self.miles)

truck1 = Truck(10, 100000, 2010, 500)
truck2 = Truck(10, 150000, 2013, 600)

trailer1 = Trailer(4, 50000, 2021, 'container')
truck1.addRepair('15-02-2023', 'Fixed engine')
truck1.addTrailer(trailer1)

driver1 = TruckDriver('Marko', 'Markovic','21-02-1993', '281839401', 30, '5 years', 40, 34)
driver2 = TruckDriver('Miomir', 'Markovic','21-02-1993', '281839401', 30, '5 years', 40, 34)
driver3 = TruckDriver('Dragoljub', 'Dragic','21-02-1993', '281839401', 30, '5 years', 40, 34)
driver1.addTruck(truck1)

managers = []
manager1 = Manager('Petar', 'Petrovic','21-02-1993', '281839401', 30, '5 years', 40, 34)
dispatcher1 = Dispatcher('Nikola', 'Nikolic','21-02-1993', '281839401', 30, '5 years', 40, 34)

driver2.addTruck(truck2)
manager1.addTruckDriver(driver1)
manager1.addDispatcher(dispatcher1)
dispatcher1.addTruckDriver(driver1)

dispatcher1.setArea('Downtown')
dispatcher1.giveDriverJob('something', driver1)

driver1.addTruck(truck1)
