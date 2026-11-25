def square(side: int):
    return side * side

def rectangle(length: int, height: int):
    return length * height

def rtriangle(side1: int, side2: int):
    return (side1 * side2) / 2

shape = str(input("Shape (square, rectangle, right triangle): ")).lower()

if shape == "square":
    side = int(input("Side: "))
    print("Area:", square(side))

elif shape == "rectangle":
    length = int(input("Length: "))
    height = int(input("Height: "))
    print("Area:", rectangle(length, height))

elif shape == "right triangle":
    side1 = int(input("Side 1: "))
    side2 = int(input("Side 2: "))
    print("Area:", rtriangle(side1, side2))

else:
    print("Not a valid shape")
