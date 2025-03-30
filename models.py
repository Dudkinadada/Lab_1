# models.py
import json
import xml.etree.ElementTree as ET
from typing import List

# Базовый класс для людей в университете
class Person:
    def __init__(self, name: str, age: int):
        if not name or not isinstance(name, str):
            raise ValueError("Имя должно быть непустой строкой")
        if age <= 0:
            raise ValueError("Возраст должен быть положительным числом")
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} лет"


class Student(Person):
    def __init__(self, name: str, age: int, student_id: str):
        super().__init__(name, age)
        if not student_id or not isinstance(student_id, str):
            raise ValueError("ID студента должно быть строкой")
        self.student_id = student_id

    def __str__(self):
        return f"{self.name}, ID: {self.student_id}"


class Professor(Person):
    def __init__(self, name: str, age: int, department: str):
        super().__init__(name, age)
        if not department or not isinstance(department, str):
            raise ValueError("Название кафедры должно быть строкой")
        self.department = department

    def __str__(self):
        return f"{self.name}, Преподаватель, Кафедра: {self.department}"


class Course:
    def __init__(self, course_name: str, course_code: str, professor: Professor):
        if not course_name or not isinstance(course_name, str):
            raise ValueError("Название курса должно быть строкой")
        if not course_code or not isinstance(course_code, str):
            raise ValueError("Код курса должен быть строкой")
        if not isinstance(professor, Professor):
            raise TypeError("Преподаватель должен быть экземпляром класса Professor")
        self.course_name = course_name
        self.course_code = course_code
        self.professor = professor
        self.students: List[Student] = []

    def add_student(self, student: Student):
        if not isinstance(student, Student):
            raise TypeError("Студент должен быть экземпляром класса Student")
        self.students.append(student)

    def remove_student(self, student: Student):
        if student not in self.students:
            raise ValueError("Студент не найден в курсе")
        self.students.remove(student)

    def __str__(self):
        return f"{self.course_name} ({self.course_code}), Преподаватель: {self.professor.name}, " \
               f"Студентов: {len(self.students)}"


class Department:
    def __init__(self, name: str):
        if not name or not isinstance(name, str):
            raise ValueError("Название факультета должно быть строкой")
        self.name = name
        self.courses: List[Course] = []

    def add_course(self, course: Course):
        if not isinstance(course, Course):
            raise TypeError("Курс должен быть экземпляром класса Course")
        self.courses.append(course)

    def __str__(self):
        return f"Факультет: {self.name}, Курсов: {len(self.courses)}"


class University:
    def __init__(self, name: str):
        if not name or not isinstance(name, str):
            raise ValueError("Название университета должно быть строкой")
        self.name = name
        self.departments: List[Department] = []

    def add_department(self, department: Department):
        if not isinstance(department, Department):
            raise TypeError("Факультет должен быть экземпляром класса Department")
        self.departments.append(department)

    def __str__(self):
        return f"Университет: {self.name}, Факультетов: {len(self.departments)}"
