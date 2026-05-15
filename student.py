from person import Person


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

    def display_information(self):
        return [
            self.__student_id,
            self.get_full_name(),
            self.__course_name,
            self.__year_level,
            self.__general_average
        ]