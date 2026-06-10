class Student:
    def __init__(self, имя, фамилия, возраст, курс):
        self.first_name = имя
        self.last_name = фамилия
        self.age = возраст
        self.course = курс

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} лет, курс: {self.course}"