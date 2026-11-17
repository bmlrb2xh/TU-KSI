class Flyer:
    def fly(self):
        print("Летя в небето")

class Swimmer:
    def swim(self):
        print("Плувам във водата")

class Duck(Flyer, Swimmer):
    pass

if __name__ == "__main__":
    d = Duck()
    d.fly()
    d.swim()
    print(Duck.__mro__)
