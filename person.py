class Person:
    def __init__(self, full_name):
        self._full_name = full_name

    def get_full_name(self):
        return self._full_name

    def set_full_name(self, updated_full_name):
        self._full_name = updated_full_name

    def display_information(self):
        print(f"Full Name: {self._full_name}")