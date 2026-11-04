def add(num1: int, num2: int):
    return num1 + num2

def sub(num1: int, num2: int):
    return num1 - num2

def mul(num1: int, num2: int):
    return num1 * num2

def div(num1: int, num2: int):
    if num2 == 0:
        print("Can't divide by 0")
        return 
    return int(num1 / num2)

operation = str(input("Operation (+, -, *, /): "))

if operation == "+":
    num1 = int(input("Number 1: "))
    num2 = int(input("Number 2: "))
    print("Added:", add(num1, num2))

elif operation == "-":
    num1 = int(input("Number 1: "))
    num2 = int(input("Number 2: "))
    print("Subtracted:", sub(num1, num2))

elif operation == "*":
    num1 = int(input("Number 1: "))
    num2 = int(input("Number 2: "))
    print("Multiplied:", mul(num1, num2))

elif operation == "/":
    num1 = int(input("Number 1: "))
    num2 = int(input("Number 2: "))
    value = div(num1, num2)
    if value != None:
        print("Divided:", value)

else:
    print("Not a valid operation")
