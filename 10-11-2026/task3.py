from task1 import Person

class Lecturer(Person):
    university: str
    experience: int

    def __init__(self, name: str, family: str, age: int, nationality: str, university: str, experience: int):
            super().__init__(name, family, age, nationality)
            self.university = university
            self.experience = experience
    
    def print(self):
        print(self.university, self.experience)

l1 = Lecturer("Ivan", "Stefanov", 23, "Bulgarian", "TU Sofia", 10)
l2 = Lecturer("Miranda", "Johnson", 50, "British", "Cambridge", 15)
l1.print()
l2.print()
