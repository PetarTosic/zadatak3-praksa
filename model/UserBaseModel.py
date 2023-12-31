class User:
  first_name: str
  last_name: str
  birthday: str
  jmbg: str
  age: int
  exp: str
  workHours: int
  
  def __init__(self, first_name: str, last_name: str, birthday: str, jmbg: str, exp: str, workHours: int):
    self.first_name = first_name
    self.last_name = last_name
    self.birthday = birthday
    self.jmbg = jmbg
    self.age = 2023 - int(birthday.split('-')[2]) 
    self.exp = exp
    self.workHours = workHours

  def __str__(self) -> str:
    return f"{self.first_name} {self.last_name}, experience: {self.exp}."