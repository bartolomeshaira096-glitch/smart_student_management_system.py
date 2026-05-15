import json

class Person:
    def __init__(self, full_name):
        self._full_name = full_name

    def get_full_name(self):
        return self._full_name

    def set_full_name(self, updated_full_name):
        self._full_name = updated_full_name

    def display_information(self):
        print(f"Full Name: {self._full_name}")

class Student(Person):
    def __init__(
        self,
        student_id,
        full_name,
        course_name,
        year_level,
        general_average
    ):
        super().__init__(full_name)

        self.__student_id = student_id
        self.__course_name = course_name
        self.__year_level = year_level
        self.__general_average = general_average

    def get_student_id(self):
        return self.__student_id

    def get_course_name(self):
        return self.__course_name

    def get_year_level(self):
        return self.__year_level

    def get_general_average(self):
        return self.__general_average

    def set_course_name(self, updated_course_name):
        self.__course_name = updated_course_name

    def set_year_level(self, updated_year_level):
        self.__year_level = updated_year_level

    def set_general_average(self, updated_general_average):
        self.__general_average = updated_general_average

    # Polymorphism (Method Overriding)
    def display_information(self):
        return [
            self.__student_id,
            self.get_full_name(),
            self.__course_name,
            self.__year_level,
            self.__general_average
        ]
    
class SmartStudentManagementSystem:
    def __init__(self):
        self.student_records = []
        self.file_name = "student_records.json"
        self.load_student_records()

    def add_student(
        self,
        student_id,
        full_name,
        course_name,
        year_level,
        general_average
    ):
        new_student = Student(
            student_id,
            full_name,
            course_name,
            year_level,
            general_average
        )

        self.student_records.append(new_student)
        self.save_student_records()