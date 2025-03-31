
from models import University, Department, Course, Professor, Student
from storage import save_to_json, load_from_json

if __name__ == "__main__":

    uni = University("Tech University")

    cs_department = Department("Computer Science")

    prof_john = Professor("John Doe", 45, "Computer Science")

    course_python = Course("Python Programming", "CS101", prof_john)

    student_anna = Student("Anna Smith", 20, "S123")
    student_bob = Student("Bob Brown", 21, "S124")

    course_python.add_student(student_anna)
    course_python.add_student(student_bob)

    cs_department.add_course(course_python)

    uni.add_department(cs_department)

    save_to_json(uni, "university.json")

    loaded_uni = load_from_json("university.json")
    print(loaded_uni)
