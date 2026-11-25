n = 0
while True:
    n = int(input("Size of triangle: "))
    if n > 0:
        break
    print("Size must be more than 0")
for i in range(n):
    print("*" * (i + 1))
