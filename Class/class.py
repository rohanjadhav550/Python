class Student:
    def __init__(self, name, rollNumber):
        self.name = name
        self.rollNumber = rollNumber

    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.rollNumber}")

std = Student('Rohan',1)

std.display()