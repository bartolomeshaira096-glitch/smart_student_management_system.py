import json
from student import Student


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

    def get_all_students(self):
        return self.student_records

    def search_student(self, student_id):
        for student_record in self.student_records:
            if student_record.get_student_id() == student_id:
                return student_record

        return None

    def update_student(
        self,
        student_id,
        full_name,
        course_name,
        year_level,
        general_average
    ):
        student_record = self.search_student(student_id)

        if student_record:
            student_record.set_full_name(full_name)
            student_record.set_course_name(course_name)
            student_record.set_year_level(year_level)
            student_record.set_general_average(
                general_average
            )

            self.save_student_records()
            return True

        return False

    def delete_student(self, student_id):
        student_record = self.search_student(student_id)

        if student_record:
            self.student_records.remove(student_record)
            self.save_student_records()
            return True

        return False

    def get_top_student(self):
        if not self.student_records:
            return None

        return min(
            self.student_records,
            key=lambda student_record:
            student_record.get_general_average()
        )

    def save_student_records(self):
        student_data = []

        for student_record in self.student_records:
            student_data.append({
                "student_id": student_record.get_student_id(),
                "full_name": student_record.get_full_name(),
                "course_name": student_record.get_course_name(),
                "year_level": student_record.get_year_level(),
                "general_average": (
                    student_record.get_general_average()
                )
            })

        with open(self.file_name, "w") as file_handler:
            json.dump(student_data, file_handler, indent=4)

    def load_student_records(self):
        try:
            with open(self.file_name, "r") as file_handler:
                student_data = json.load(file_handler)

            for student_information in student_data:
                loaded_student = Student(
                    student_information["student_id"],
                    student_information["full_name"],
                    student_information["course_name"],
                    student_information["year_level"],
                    student_information["general_average"]
                )

                self.student_records.append(
                    loaded_student
                )

        except FileNotFoundError:
            pass