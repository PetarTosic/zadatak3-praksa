from model.UserModel import TruckDriver, Dispatcher, Manager
from model.UserBaseModel import User
from model.VehicleModel import Truck

def addTruck(driver: TruckDriver, truck: Truck):
    driver.truck = truck
    truck.truckDriver = driver

def addManager(user: User, mng: str):
    user.manager = mng

def setArea(user: User, area: str):
    user.area = area

def addDispatcher(driver: TruckDriver, disp: Dispatcher):
    driver.dispatcher = disp

def addLoadAndArea(driver: TruckDriver, load: str, area: str):
    if not driver.truck and not driver.truck.trailer:
      driver.load = load
      driver.area = area
    else:
      print('Driver doesn\'t have truck and/or trailer.')

def addTruckDriver(user: User, driver: TruckDriver):
    user.truckDrivers.append(driver)
    if(type(user) == Dispatcher):  
      driver.dispatcher = user
    else:
      driver.manager = user.jmbg

def giveDriverJob(disp: Dispatcher, load: str, driver: dict):
    if driver not in disp.truckDrivers:
      disp.truckDrivers.append(driver)
    addLoadAndArea(driver, load, disp.area)

def showTruckDrivers(user: User):
    if len(user.truckDrivers) > 0:
      for driver in user.truckDrivers:
        print(driver)
    else:
      print('No drivers assigned.')

def addDispatcher(manager: Manager, disp: Dispatcher):
    manager.dispatchers.append(disp)
    addManager(disp, manager)
    if manager.area:
      setArea(disp, manager.area)
