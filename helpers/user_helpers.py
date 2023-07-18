def addTruck(driver: dict, truck: dict):
    driver.truck = truck
    truck.truckDriver = driver

def addManager(user: dict, mng: str):
    user.manager = mng

def setArea(user: dict, area: str):
    user.area = area

def addDispatcher(driver: dict, disp: dict):
    driver.dispatcher = disp

def addLoadAndArea(driver: dict, load: str, area: str):
    if driver.truck != {} and driver.truck.trailer != {}:
      driver.load = load
      driver.area = area
    else:
      print('Driver doesn\'t have truck and/or trailer.')

def addTruckDriver(user: dict, driver: dict):
    user.truckDrivers.append(driver)
    if(type(user) == Dispatcher):  
      driver.dispatcher = user
    else:
      driver.manager = user.jmbg

def giveDriverJob(disp: dict, load: str, driver: dict):
    if driver not in disp.truckDrivers:
      disp.truckDrivers.append(driver)
    addLoadAndArea(driver, load, disp.area)

def showTruckDrivers(user: dict):
    if len(user.truckDrivers) > 0:
      for driver in user.truckDrivers:
        print(driver)
    else:
      print('No drivers assigned.')

def addDispatcher(manager: dict, disp: dict):
    manager.dispatchers.append(disp)
    addManager(disp, manager)
    if manager.area:
      setArea(disp, manager.area)
