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
