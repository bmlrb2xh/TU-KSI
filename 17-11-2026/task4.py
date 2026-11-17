class Person:
    name: str
    age: int

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

class Student(Person):
    faculty_number: str

    def __init__(self, name: str, age: int, faculty_number: str):
        super().__init__(name, age)
        self.faculty_number = faculty_number
