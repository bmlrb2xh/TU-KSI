n = 0
while True:
    n = int(input("Number of numbers: "))
    if n > 0:
        break
    print("Number must be more than 0")
s = 0
for i in range(n):
    s += int(input(f"Number {i + 1}: "))
print(f"Sum: {s}")
