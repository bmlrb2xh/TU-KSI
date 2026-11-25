from math_operations import add, sub, mul, div

def main():
    print("Available operations: 'add' 'sub' 'mul' 'div'")
    print("Press [Ctrl + C] to stop the program")
    res: float
    while True:
        operation = str(input("Pick operation: "))
        try:
            if operation == "add":
                num1 = float(input("Number 1: "))
                num2 = float(input("Number 2: "))
                res = add(num1, num2)
            elif operation == "sub":
                num1 = float(input("Number 1: "))
                num2 = float(input("Number 2: "))
                res = sub(num1, num2)
            elif operation == "mul":
                num1 = float(input("Number 1: "))
                num2 = float(input("Number 2: "))
                res = mul(num1, num2)
            elif operation == "div":
                num1 = float(input("Number 1: "))
                num2 = float(input("Number 2: "))
                res = div(num1, num2)
            else:
                print("Invalid operation")
                continue
            print("Result:", res)
        except ArithmeticError:
            print("Couldn't calculate :(")
        except Exception as ex:
            print("An unexpected error")
            print(ex)

if __name__ == "__main__":
    main()
