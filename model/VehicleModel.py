from pydantic import Field
from typing import Union
from model.VehicleBaseModel import Vehicle

class Truck(Vehicle):
  truckDriver: Union[dict, None] = Field(
    default=None,
    description="Truck driver that drives this truck."
  )
  trailer: Union[dict, None] = Field(
    default=None,
    description="Trailer that this truck is truckin."
  )

  def __init__(self, wheels: int, miles: int, year: int, horsepower: int):
    super().__init__(wheels, miles, year)
    self.horsepower = horsepower
    self.truckDriver = {}
    self.trailer = {}
  
  def __str__(self)-> str:
    return f'{self.year} Truck with: {self.wheels} wheels and {self.miles} miles.'


class Trailer(Vehicle):
  truck: Union[dict, None] = Field(
    default=None,
    description="Truck that is towin this trailer."
  )

  def __init__(self, wheels: int, miles: int, year: int, type: str):
    super().__init__(wheels, miles, year)
    self.type = type
    self.truck = {}

  def __str__(self)-> str:
    return f'{self.year} Trailer with: {self.wheels} wheels and {self.miles} miles.'
