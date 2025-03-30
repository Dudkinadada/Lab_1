# storage.py
import json
import xml.etree.ElementTree as ET
from models import University, Department, Course, Professor, Student


def save_to_json(university: University, filename: str):
    data = {
        "university": university.name,
        "departments": []
    }
    for department in university.departments:
        dept_data = {
            "name": department.name,
            "courses": []
        }
        for course in department.courses:
            course_data = {
                "course_name": course.course_name,
                "course_code": course.course_code,
                "professor": course.professor.name,
                "students": [student.name for student in course.students]
            }
            dept_data["courses"].append(course_data)
        data["departments"].append(dept_data)

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def load_from_json(filename: str) -> University:
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)

    university = University(data['university'])
    for dept_data in data['departments']:
        department = Department(dept_data['name'])
        for course_data in dept_data['courses']:
            professor = Professor(course_data['professor'], 0, "")
            course = Course(course_data['course_name'], course_data['course_code'], professor)
            for student_name in course_data['students']:
                student = Student(student_name, 0, "")
                course.add_student(student)
            department.add_course(course)
        university.add_department(department)
    return university
