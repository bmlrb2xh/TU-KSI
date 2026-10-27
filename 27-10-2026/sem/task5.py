n = int(input("Number of numbers: "))
power = float(input("Power: "))
arr = list()
for i in range(n):
    arr.append(pow(int(input(f"Number {i + 1}: ")), power))
print(arr)
