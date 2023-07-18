class Vehicle:
  wheels: int
  miles: int
  year: int

  def __init__(self, wheels: int, miles: int, year: int):
    self.wheels = wheels
    self.miles = miles
    self.year = year
    self.repairs = []

  def addRepair(self, date, description):
    self.repairs.append(Repair(date, description, self))

  def showRepairs(self):
    for repair in self.repairs:
      print(repair)


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