class Course:
    def __init__(self, course_name, course_code):
        self.course_name = course_name
        self.course_code = course_code
        self.students = []

    def enroll_student(self, student):
        self.students.append(student)
        print(f"Student {student.name} enrolled in {self.course_name}")

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def enroll(self, course):
        course.enroll_student(self)

class Teacher:
    def __init__(self, name, teacher_id):
        self.name = name
        self.teacher_id = teacher_id

    def assign_course(self, course):
        self.course = course
        print(f"Teacher {self.name} assigned to {course.course_name}")

# Example Usage
math = Course("Mathematics", "MATH101")
john = Student("John Doe", 1001)
teacher = Teacher("Mr. Smith", 5001)

john.enroll(math)
teacher.assign_course(math)
