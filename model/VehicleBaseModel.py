class Vehicle:
  wheels: int
  miles: int
  year: int

  def __init__(self, wheels: int, miles: int, year: int):
    self.wheels = wheels
    self.miles = miles
    self.year = year
    self.repairs = []


class Repair:
  date: str
  description: str
  subject: object

  def __init__(self, date: str, description: str, subject: object):
    self.date = date
    self.description = description
    self.subject = subject
  
  def __str__(self)-> str:
    return f'{self.date}: {self.description}'