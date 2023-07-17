class Vehicle:
  wheels: int
  miles: int
  year: int

  def __init__(self, wheels, miles, year):
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

  def __init__(self, date, description, subject):
    self.date = date
    self.description = description
    self.subject = subject
  
  def __str__(self):
    return "{}: {}".format(self.date, self.description)