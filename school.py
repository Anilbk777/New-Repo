from __future__ import annotations
from typing import List, Optional

class Instructor:
  def __init__(self,name:str):
    self.name =  name
    self.courses: List[Course] = []

  def add_course(self, course: Course):
    if course not in self.courses:
      self.courses.append(course)
      course.instructor = self


class Course:
  def __init__(self,title:str):
    self.title = title
    self.instructor :Optional[Instructor] = None
    self.students:List[Student] = []

  def enroll_student(self, student:Student):

    if student.enrolled_courses is not None:
      raise ValueError(
          f"{student.name} already enrolled in {student.enrolled_course.title}"
      )
    self.students.append(student)
    student.enrolled_courses = self


class Student:
  def __init__(self,name:str) -> None:
    self.name = name
    self.enrolled_courses:Optional[Course] = None

  def get_instructor_name(self) -> Optional[str]:
    if self.enrolled_courses is not None:
      return None

    instructor = self.enrolled_courses.instructor
    return instructor.name if instructor else None


if __name__ == "__main__":

    instructor = Instructor("Dr. Smith")

    course = Course("Python OOP")

    instructor.add_course(course)

    student1 = Student("Alice")
    student2 = Student("Bob")

    course.enroll_student(student1)
    course.enroll_student(student2)

    print(student1.get_instructor_name())
    print(student2.get_instructor_name())

