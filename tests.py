# tests.py
import unittest
from models import University, Department, Course, Professor, Student


class TestUniversitySystem(unittest.TestCase):
    def setUp(self):
        self.university = University("Test University")
        self.department = Department("Computer Science")
        self.professor = Professor("Dr. Smith", 50, "Computer Science")
        self.course = Course("Algorithms", "CS102", self.professor)
        self.student = Student("Alice", 22, "S001")

    def test_student_creation(self):
        self.assertEqual(self.student.name, "Alice")
        self.assertEqual(self.student.student_id, "S001")

    def test_add_course_to_department(self):
        self.department.add_course(self.course)
        self.assertIn(self.course, self.department.courses)

    def test_add_student_to_course(self):
        self.course.add_student(self.student)
        self.assertIn(self.student, self.course.students)

    def test_remove_student_from_course(self):
        self.course.add_student(self.student)
        self.course.remove_student(self.student)
        self.assertNotIn(self.student, self.course.students)

    def test_university_structure(self):
        self.university.add_department(self.department)
        self.assertIn(self.department, self.university.departments)


if __name__ == '__main__':
    unittest.main()
