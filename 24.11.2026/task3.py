num = int(input())

try:
    if num < 0:
        raise Exception
    print(num ** 0.5)
except:
    print("Invalid Number")
finally:
    print("Good Bye")
