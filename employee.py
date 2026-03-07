
from __future__ import annotations

class Employee:
  def __init__(self, name:str, role:str):
    self._name = name
    self._role = role
    self._teams: list[Team]= []

  # def add_team(self, team:Team):
  #   if team in self._teams:
  #     raise ValueError(f"Employee {self._name} is already in this team {team._name}")
  #   self._teams.append(team)

  # def remove_team(self, team:Team):
  #   if team not in self._teams:
  #     raise ValueError(f"{self._name} is not in the team {team._name}")

  #   self._teams.remove(team)

  def add_team(self, team: Team):
    self._teams.append(team)

  def remove_team(self, team: Team):
    self._teams.remove(team)


  @property
  def name(self) -> str:
    return self._name

  @property
  def role(self) -> str:
    return self._role

  @property
  def teams(self) -> list[Team]:
    return list(self._teams)

  def get_team_names(self) -> list:
    return [team.name for team in self.teams]


  def __repr__(self):
    return f"Employee(name ={self._name!r}, role={self._role!r}, teams ={self.get_team_names()})"


class Team:
  def __init__(self,name:str):
    self._name = name
    self._members: list[Employee] = []

  def add_member(self, employee: Employee):
    if employee in self._members:
      raise ValueError(f"{employee.name} is already in the team {self._name}")

    self._members.append(employee)
    employee.add_team(self)

  def remove_member(self, employee: Employee):
    if employee not in self._members:
      raise ValueError(f"{employee.name} is not in the team {self._name}")
    self._members.remove(employee)
    employee.remove_team(self)

  def dissolve(self):
    for emp in self._members:
      emp.remove_team(self)
    self._members.clear()

  def get_member_count(self) -> int:
    return len(self._members)

  @property
  def name(self):
    return self._name

  @property
  def members(self):
    return list(self._members)


  def __repr__(self):
    return f"Team(name ={self._name!r}, members ={self.members!r})"

class Company:
    def __init__(self, name: str):
        self._name = name
        self._employees: list[Employee] = []
        self._teams:list[Team] = []

    def add_employee(self, employee: Employee):
        if employee in self._employees:
          raise ValueError(f"{employee.name} is already in the company {self._name}.")

        self._employees.append(employee)

    def add_team(self, team: Team):
        if team in self._teams:
          raise ValueError(f"{team.name} is already in the company {self._name}.")

        self._teams.append(team)

    def dissolve_team(self, team: Team):
        if team not in self._teams:
          raise ValueError(f"{team.name} is not in the company {self._name}")
        team.dissolve()
        self._teams.remove(team)

    @property
    def teams(self):
      return list(self._teams)

    def get_employee_count(self):
        return len(self._employees)

    def get_team_count(self):
        return len(self._teams)

    def __repr__(self):
      return f"Company(name={self._name!r}, employees={self.get_employee_count()}, teams={self.get_team_count()})"


if __name__ == "__main__":
    company = Company("TechCorp")
    company2 = Company("abc company")

    alice = Employee("Alice", "Engineer")
    bob = Employee("Bob", "Designer")
    charlie = Employee("Charlie", "Engineer")

    company.add_employee(alice)
    company.add_employee(bob)
    company.add_employee(charlie)

    backend = Team("Backend")
    frontend = Team("Frontend")

    company.add_team(backend)
    company.add_team(frontend)

    backend.add_member(alice)
    backend.add_member(charlie)
    frontend.add_member(alice)
    frontend.add_member(bob)

    print("Before dissolving:")
    print(f"  {alice.name}'s teams: [{', '.join(alice.get_team_names())}]")
    print(f"  Backend has {backend.get_member_count()} members")
    print(f"  Company has {company.get_team_count()} teams, {company.get_employee_count()} employees")

    company.dissolve_team(backend)

    print("\nAfter dissolving Backend:")
    print(f"  {alice.name}'s teams: [{', '.join(alice.get_team_names())}]")
    print(f"  {charlie.name}'s teams: [{', '.join(charlie.get_team_names())}]")
    print(f"  Company has {company.get_team_count()} teams, {company.get_employee_count()} employees")
    print(f"  {alice.name} still exists: {alice.role}")
