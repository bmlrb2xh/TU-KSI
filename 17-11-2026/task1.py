class Person:
    name: str
    age: int

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Здравей, аз съм {self.name} и съм на {self.age} години.")

if __name__ == "__main__":
    p1 = Person("Michael", 34)
    p2 = Person("Chris", 25)
    p1.introduce()
    p2.introduce()
