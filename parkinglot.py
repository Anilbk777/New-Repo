class ParkingSpot:
    def __init__(self, spot_id: str):
        self.spot_id = spot_id
        self._employee = None  # back-reference

    def __repr__(self):
        return f"ParkingSpot({self.spot_id})"

    @property
    def employee(self):
        return self._employee


class Employee:
    def __init__(self, name: str):
        self.name = name
        self._spot: ParkingSpot | None = None

    def assign_spot(self, spot: ParkingSpot):
        # Unlink old spot if exists
        if self._spot:
            self._spot._employee = None
        self._spot = spot
        spot._employee = self  # keep both sides in sync

    def __repr__(self):
        spot = self._spot.spot_id if self._spot else "None"
        return f"Employee({self.name}, spot={spot})"


# Usage
emp = Employee("Bob")
spot = ParkingSpot("A-42")
emp.assign_spot(spot)

print(emp)           # Employee(Bob, spot=A-42)
# print(spot.employee) # Employee(Bob, spot=A-42)

spot2 = ParkingSpot("B-44")
emp.assign_spot(spot2)
print(emp)

