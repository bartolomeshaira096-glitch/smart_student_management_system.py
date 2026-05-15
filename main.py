import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from smart_student_management_system import (
    SmartStudentManagementSystem
)

class StudentManagementApplication:
    def __init__(self, application_window):
        self.application_window = (
            application_window
        )

        self.student_management_system = (
            SmartStudentManagementSystem()
        )

        self.application_window.title(
            "Smart Student Management System"
        )
        self.application_window.geometry(
            "900x550"
        )

        self.create_input_fields()
        self.create_buttons()
        self.create_student_table()
        self.refresh_student_table()

    
    def create_input_fields(self):
        input_frame = tk.Frame(
            self.application_window
        )
        input_frame.pack(pady=10)

        tk.Label(
            input_frame,
            text="Student ID"
        ).grid(row=0, column=0)

        self.student_id_entry = tk.Entry(
            input_frame
        )
        self.student_id_entry.grid(
            row=0,
            column=1,
            padx=10
        )

        tk.Label(
            input_frame,
            text="Full Name"
        ).grid(row=1, column=0)

        self.full_name_entry = tk.Entry(
            input_frame,
            width=30
        )
        self.full_name_entry.grid(
            row=1,
            column=1,
            padx=10
        )

        tk.Label(
            input_frame,
            text="Course Name"
        ).grid(row=2, column=0)

        self.course_name_entry = tk.Entry(
            input_frame,
            width=30
        )
        self.course_name_entry.grid(
            row=2,
            column=1,
            padx=10
        )

        tk.Label(
            input_frame,
            text="Year Level"
        ).grid(row=3, column=0)

        self.year_level_entry = tk.Entry(
            input_frame
        )
        self.year_level_entry.grid(
            row=3,
            column=1,
            padx=10
        )

        tk.Label(
            input_frame,
            text="General Average"
        ).grid(row=4, column=0)

        self.general_average_entry = tk.Entry(
            input_frame
        )
        self.general_average_entry.grid(
            row=4,
            column=1,
            padx=10
        )

    def create_buttons(self):
        button_frame = tk.Frame(
            self.application_window
        )
        button_frame.pack(pady=10)

        tk.Button(
            button_frame,
            text="Add Student",
            command=self.add_student
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            button_frame,
            text="Update Student",
            command=self.update_student
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            button_frame,
            text="Delete Student",
            command=self.delete_student
        ).grid(row=0, column=2, padx=5)

        tk.Button(
            button_frame,
            text="Search Student",
            command=self.search_student
        ).grid(row=0, column=3, padx=5)

        tk.Button(
            button_frame,
            text="Top Student",
            command=self.display_top_student
        ).grid(row=0, column=4, padx=5)

        tk.Button(
            button_frame,
            text="Clear Fields",
            command=self.clear_input_fields
        ).grid(row=0, column=5, padx=5)


