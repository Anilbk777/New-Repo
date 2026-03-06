class Employee:
  def __init__(self, name:str):
    self.name = name
    self._department: " Department | None" = None

  @property
  def department(self):
    return str(self._department)

  def __repr__(self):
    dpt = self._department.name if self._department else None
    return f"Employee(name={self.name}, department ={dpt})"


class Department:
  def __init__(self, name):
    self.name =  name
    self._employees: List[Employee] = []

  def add_employee(self, emp: Employee):
    if emp in self._employees:
      raise ValueError("Employee already exist in this department")
    self._employees.append(emp)
    emp._department = self

  def remove_employee(self, empt: Employee):
    if emp not in self._employees:
      raise ValueError("Employee don't exist in this department")

    self._employees.remove(empt)
    empt._department = None

  @property
  def employees(self):
    return list(self._employees)

  def __repr__(self):
    return f"Department(name = {self.name}, employees={self.employees})"


dept = Department("Engineering")
alice = Employee("Alice")
bob = Employee("Bob")

dept.add_employee(alice)
dept.add_employee(bob)

print(dept)          # Department(Engineering, employees=['Alice', 'Bob'])
print(alice)         # Employee(Alice, dept=Engineering)
print(bob.department)# Department(Engineering, ...)
