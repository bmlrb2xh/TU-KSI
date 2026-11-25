class Counter:
    value: int

    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def show(self):
        print(self.value)

if __name__ == "__main__":
    c1 = Counter()
    c2 = Counter()
    c1.increment()
    c1.increment()
    c2.increment()
    c1.show()
    c2.show()
