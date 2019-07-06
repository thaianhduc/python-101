import random

# Define the function first. The execution is top down

class Student():
    static_field = "A static field"
    def __init__(self, name):
        """
        Constructor
        :param name: string - student name
        """
        self.name = name

    def __str__(self):
        return self.name

    def getName(self):
        return self.name

class DerivedStudent(Student):
    static_field = "A derived class"

mark = Student("Mark and Jane")
print(mark)
print(Student.static_field)
print(DerivedStudent.static_field)