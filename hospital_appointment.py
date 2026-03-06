# Hospital Appointment System
from __future__ import annotations
from datetime import datetime, timezone, timedelta
from typing import List

class Room:
  def __init__(self,number:int, floor:int) -> None:
    self.number = number
    self.floor = floor


class Appointment:

  def __init__(self, room: Room, doctor: Doctor, patient: Patient, time:str) -> None:
    self.room = room
    self.doctor = doctor
    self.patient = patient
    # self.time = datetime.now(timezone(timedelta(hours=5, minutes=45)))
    self.time = time

    doctor.add_appointment(self)
    patient.add_appointment(self)

  def display(self):
        print(
            f"{self.time} | {self.doctor.name} with {self.patient.name} in {self.room.number}"
        )


class Doctor:
  def __init__(self, name:str, specialization:str):
    self.name = name
    self.specialization = specialization
    self.appointments: List[Appointment]= []

  def add_appointment(self, appt: Appointment):
    self.appointments.append(appt)

  def get_patients(self) -> List["Patient"]:
    result = [appt_obj.patient.name for appt_obj in self.appointments ]
    return result



class Patient:
  def __init__(self,name:str):
    self.name = name
    self.appointments: List[Appointment] = []

  def add_appointment(self, appt:Appointment):
    self.appointments.append(appt)

  def get_doctors(self) -> List[Doctor]:
    result = [appt_obj.doctor.name for appt_obj in self.appointments ]
    return result



if __name__ == "__main__":

    doctor = Doctor("Dr. Smith","General")
    patient = Patient("John Doe")
    room = Room(101, 2)

    doctor2= Doctor("Dr. Bob","General")
    patient2 = Patient("Alex")
    room2 = Room(102, 1)


    appt = Appointment(room, doctor, patient, "10:00 AM")
    appt2 = Appointment(room2, doctor2, patient2, "11:00 AM")
    appt3 = Appointment(room, doctor, patient2, "12:00 PM")


    output = doctor.get_patients()
    print(output)

    output2 = patient.get_doctors()
    print(output2)

    output3 = patient2.get_doctors()
    print(output3)
    output4 = doctor2.get_patients()
    print(output4)

    appt.display()
    appt2.display()
    appt3.display()

    # print("\nDoctor Schedule:")
    # for a in doctor.appointments:
    #     a.display()

    # print("\nPatient Appointments:")
    # for a in patient.appointments:
    #     a.display()

