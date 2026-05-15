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

        