class Person:
    def __init__(self, name):
        self._full_name = name

    def get_full_name(self):
        return self._full_name

    def set_full_name(self, name):
        self._full_name = name