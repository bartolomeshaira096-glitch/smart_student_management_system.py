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