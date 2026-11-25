class Person:
    name: str
    family: str
    age: int
    nationality: str

    def __init__(self, name: str, family: str, age: int, nationality: str):
        self.name = name
        self.family = family
        self.age = age
        self.nationality = nationality

    def print(self):
        print(self.name, self.nationality)

p1 = Person("Ivan", "Stefanov", 23, "Bulgarian")
p2 = Person("Miranda", "Johnson", 50, "British")
p1.print()
p2.print()
