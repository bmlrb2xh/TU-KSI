n = float(input("Lower limit: "))
m = float(input("Upper limit: "))
num = float(input("Your number: "))
print("It's in the range" if num.__ge__(n).__and__(num.__le__(m)) else "It's out of the range")
