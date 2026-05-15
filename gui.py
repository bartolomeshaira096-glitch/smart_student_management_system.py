import tkinter as tk
from tkinter import ttk, messagebox
from student_management_system import SmartStudentManagementSystem


class StudentManagementApplication:
    def __init__(self, window):
        self.window = window
        self.system = SmartStudentManagementSystem()

        self.window.title("Smart Student Management System")
        self.window.geometry("900x550")

        self.create_input_fields()
        self.create_buttons()
        self.create_table()
        self.refresh_table()

    # INPUT FIELDS
    def create_input_fields(self):
        frame = tk.Frame(self.window)
        frame.pack(pady=10)

        self.student_id = tk.Entry(frame)
        self.full_name = tk.Entry(frame)
        self.course = tk.Entry(frame)
        self.year = tk.Entry(frame)
        self.average = tk.Entry(frame)

        tk.Label(frame, text="ID").grid(row=0, column=0)
        self.student_id.grid(row=0, column=1)

        tk.Label(frame, text="Name").grid(row=1, column=0)
        self.full_name.grid(row=1, column=1)

        tk.Label(frame, text="Course").grid(row=2, column=0)
        self.course.grid(row=2, column=1)

        tk.Label(frame, text="Year").grid(row=3, column=0)
        self.year.grid(row=3, column=1)

        tk.Label(frame, text="Average").grid(row=4, column=0)
        self.average.grid(row=4, column=1)

    # BUTTONS
    def create_buttons(self):
        frame = tk.Frame(self.window)
        frame.pack(pady=10)

        tk.Button(frame, text="Add", command=self.add).grid(row=0, column=0)
        tk.Button(frame, text="Update", command=self.update).grid(row=0, column=1)
        tk.Button(frame, text="Delete", command=self.delete).grid(row=0, column=2)
        tk.Button(frame, text="Search", command=self.search).grid(row=0, column=3)

    # TABLE
    def create_table(self):
        self.table = ttk.Treeview(
            self.window,
            columns=("id", "name", "course", "year", "avg"),
            show="headings"
        )

        for col in ("id", "name", "course", "year", "avg"):
            self.table.heading(col, text=col)

        self.table.pack(fill="both", expand=True)

    # ACTION METHODS
    def add(self):
        try:
            self.system.add_student(
                self.student_id.get(),
                self.full_name.get(),
                self.course.get(),
                int(self.year.get()),
                float(self.average.get())
            )
            self.refresh_table()
        except:
            messagebox.showerror("Error", "Invalid input")

    def update(self):
        self.system.update_student(
            self.student_id.get(),
            self.full_name.get(),
            self.course.get(),
            int(self.year.get()),
            float(self.average.get())
        )
        self.refresh_table()

    def delete(self):
        self.system.delete_student(self.student_id.get())
        self.refresh_table()

    def search(self):
        student = self.system.search_student(self.student_id.get())
        if student:
            messagebox.showinfo("Found", student.get_full_name())

    def refresh_table(self):
        for row in self.table.get_children():
            self.table.delete(row)

        for s in self.system.get_all_students():
            self.table.insert("", "end", values=s.display_information())