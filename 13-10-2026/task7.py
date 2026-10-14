a = float(input("Number 1: "))
b = float(input("Number 2: "))
operator = str(input("Operator(sum/sub/mul/div): "))
while True:
    if operator == "sum":
        print(a + b)
        break
    elif operator == "sub":
        print(a - b)
        break
    elif operator == "mul":
        print(a * b)
        break
    elif operator == "div" and b == 0:
        print("Can't divide by 0")
        b = float(input("Pick a different value for Number 2: "))
    elif operator == "div":
        print(a / b)
        break
    else:
        print("Invalid operator")
        operator = str(input("Operator(sum/sub/mul/div): "))
