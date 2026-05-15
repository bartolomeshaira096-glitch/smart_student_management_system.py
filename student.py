from person import Person


class Student(Person):
    def __init__(self, id, name, course, year, avg):
        super().__init__(name)
        self.id = id
        self.course = course
        self.year = year
        self.avg = avg

    def get_student_id(self):
        return self.id

    def get_course_name(self):
        return self.course

    def get_year_level(self):
        return self.year

    def get_general_average(self):
        return self.avg

    def set_course_name(self, c):
        self.course = c

    def set_year_level(self, y):
        self.year = y

    def set_general_average(self, a):
        self.avg = a

    def display_information(self):
        return [self.id, self._full_name, self.course, self.year, self.avg]