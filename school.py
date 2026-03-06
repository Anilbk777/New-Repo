from __future__ import annotations
from typing import List, Optional


class Instructor:
    def __init__(self, name: str):
        self.name = name
        self.courses: List[Course] = []

    def add_course(self, course: Course) -> None:
        if course not in self.courses:
            self.courses.append(course)
            course.set_instructor(self)

    def get_students(self) -> list[str]:
      students = set()

      for course in self.courses:
          for student in course.students:
              students.add(student.name)

      return list(students)


class Course:
    def __init__(self, title: str):
        self.title = title
        self.instructor: Optional[Instructor] = None
        self.students: set[Student] = set()

    def set_instructor(self, instructor: Instructor) -> None:
        if self.instructor is not None and self.instructor != instructor:
            raise ValueError("Course already has an instructor.")
        self.instructor = instructor

    def enroll_student(self, student: Student) -> None:
      if student not in self.students:
          self.students.add(student)
          student.courses.add(self)

class Student:
    def __init__(self, name: str):
        self.name = name
        self.courses: set[Course] = set()


    def get_instructor_names(self) -> list[str]:
      return [
          course.instructor.name
          for course in self.courses
          if course.instructor is not None
      ]


if __name__ == "__main__":

    instructor = Instructor("Dr. Smith")
    instructor2 = Instructor("Dr. Ram")

    course = Course("Python OOP")
    course2 = Course("DSA")

    instructor.add_course(course)
    instructor2.add_course(course2)

    student1 = Student("Alice")
    student2 = Student("Bob")
    student3 = Student("john")


    course.enroll_student(student1)
    course.enroll_student(student2)
    course2.enroll_student(student3)

    print(student1.get_instructor_name())
    print(student2.get_instructor_name())
    print(student3.get_instructor_name())
    instructor.get_student()
