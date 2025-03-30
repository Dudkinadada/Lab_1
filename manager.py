# main.py
from models import University, Department, Course, Professor, Student
from storage import save_to_json, load_from_json

if __name__ == "__main__":
    # Создаем университет
    uni = University("Tech University")

    # Создаем факультет
    cs_department = Department("Computer Science")

    # Создаем преподавателя
    prof_john = Professor("John Doe", 45, "Computer Science")

    # Создаем курс
    course_python = Course("Python Programming", "CS101", prof_john)

    # Создаем студентов
    student_anna = Student("Anna Smith", 20, "S123")
    student_bob = Student("Bob Brown", 21, "S124")

    # Добавляем студентов в курс
    course_python.add_student(student_anna)
    course_python.add_student(student_bob)

    # Добавляем курс на факультет
    cs_department.add_course(course_python)

    # Добавляем факультет в университет
    uni.add_department(cs_department)

    # Сохранение в JSON
    save_to_json(uni, "university.json")

    # Загрузка из JSON
    loaded_uni = load_from_json("university.json")
    print(loaded_uni)
