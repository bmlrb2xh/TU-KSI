from task1 import Person

class Student(Person):
    university: str
    yearofstudy: int

    def __init__(self, name: str, family: str, age: int, nationality: str, university: str, yearofstudy: int):
        super().__init__(name, family, age, nationality)
        self.university = university
        self.yearofstudy = yearofstudy

    def print(self):
        print(self.university, self.yearofstudy)

s1 = Student("Ivan", "Stefanov", 23, "Bulgarian", "TU Sofia", 3)
s2 = Student("Miranda", "Johnson", 50, "British", "Cambridge", 1)
s1.print()
s2.print()
