from pydantic import Field
from typing import Union
from model.UserBaseModel import User

class TruckDriver(User):
  manager_jmbg: Union[str, None] = Field(
    default=None,
    description="Truck drivers Manager."
  )
  dispatcher: Union[dict, None] = Field(
    default=None,
    description="Truck drivers dispatcher."
  )
  truck: Union[dict, None] = Field(
    default=None,
    description="Drivers truck."
  )
  area: Union[str, None] = Field(
    default=None,
    description="The area where the driver works."
  )

  def __init__(self, first_name: str, last_name: str, birthday: str, jmbg: str, exp: str, workHours: int, pay: int):
    super().__init__(first_name, last_name, birthday, jmbg, exp, workHours)
    self.payPerMile = pay
    self.manager_jmbg = ""
    self.dispatcher = {}
    self.truck = {}
    self.area = ""


class Dispatcher(User):
  manager: Union[str, None] = Field(
    default=None,
    description="Truck drivers Manager."
  )
  truckDrivers: Union[list[TruckDriver], None] = Field(
    default=None,
    description="Truck drivers that the dispatcher dispatches."
  )
  area: Union[str, None] = Field(
    default=None,
    description="The area where the driver works."
  )

  def __init__(self, first_name: str, last_name: str, birthday: str, jmbg: str, exp: str, workHours: int, pay: int):
    super().__init__(first_name, last_name, birthday, jmbg, exp, workHours)
    self.payPerMonth = pay
    self.truckDrivers = []
    self.manager = ""
    self.area = ""

  
class Manager(User):
  truckDrivers: Union[list[TruckDriver], None] = Field(
    default=None,
    description="Truck drivers that the manager manages."
  )

  dispatchers: Union[list[TruckDriver], None] = Field(
    default=None,
    description="Dispatchers that the manager manages."
  )
  area: Union[str, None] = Field(
    default=None,
    description="The area where the driver works."
  )

  def __init__(self, first_name, last_name, birthday, jmbg, exp, workHours, pay):
    super().__init__(first_name, last_name, birthday, jmbg, exp, workHours)
    self.payPerMonth = pay
    self.truckDrivers = []
    self.dispatchers = []
    self.area = ""