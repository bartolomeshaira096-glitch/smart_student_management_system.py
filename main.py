import tkinter as tk
from gui import StudentManagementApplication

def main():
    root = tk.Tk()
    app = StudentManagementApplication(root)
    root.mainloop()

if __name__ == "__main__":
    main()