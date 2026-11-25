class Car:
    brand: str
    horsepower: int

    def __init__(self, brand: str, horsepower: int):
        self.brand = brand
        self.horsepower = horsepower

    def __str__(self):
        return str("красив текстов низ")

if __name__ == "__main__":
    c1 = Car("Mercedes", 180)
    print(c1)
