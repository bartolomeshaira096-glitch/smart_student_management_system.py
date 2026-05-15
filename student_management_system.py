import json
from student import Student


class SmartStudentManagementSystem:
    def __init__(self):
        self.students = []
        self.file = "student_records.json"
        self.load()

    def add_student(self, id, name, course, year, avg):
        self.students.append(Student(id, name, course, year, avg))
        self.save()

    def update_student(self, id, name, course, year, avg):
        s = self.search_student(id)
        if s:
            s.set_full_name(name)
            s.set_course_name(course)
            s.set_year_level(year)
            s.set_general_average(avg)
            self.save()

    def delete_student(self, id):
        s = self.search_student(id)
        if s:
            self.students.remove(s)
            self.save()

    def search_student(self, id):
        for s in self.students:
            if s.get_student_id() == id:
                return s
        return None

    def get_all_students(self):
        return self.students

    def save(self):
        data = [s.display_information() for s in self.students]
        with open(self.file, "w") as f:
            json.dump(data, f, indent=4)

    def load(self):
        try:
            with open(self.file, "r") as f:
                data = json.load(f)
                for d in data:
                    self.students.append(Student(*d))
        except:
            pass