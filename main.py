# Створити ієрархію класів для опису академії.
# Зразковий список класів: Person, Teacher, Student, Subject, Academy і т.д.
#
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def display_info(self):
#         print(f'Name: {self.name}')
#
#
# class Teacher(Person):
#     def __init__(self, name, subject):
#         super().__init__(name)
#         self.subject = subject
#
#     def display_info(self):
#         super().display_info()
#         print(f'Teacher of {self.subject}')
#
#
# class Student(Person):
#     def __init__(self, name, grade):
#         super().__init__(name)
#         self.grade = grade
#
#     def display_info(self):
#         super().display_info()
#         print(f'Grade: {self.grade}')
#
#
# class Subject:
#     def __init__(self, name):
#         self.name = name
#
#
# class Academy:
#     def __init__(self, name):
#         self.name = name
#         self.teachers = []
#         self.students = []
#         self.subjects = []
#
#     def add_teacher(self, teacher):
#         self.teachers.append(teacher)
#
#     def add_student(self, student):
#         self.students.append(student)
#
#     def add_subject(self, subject):
#         self.subjects.append(subject)
#
#
