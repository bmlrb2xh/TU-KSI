n = 0
while True:
    n = int(input("Number of numbers: "))
    if n > 0:
        break
    print("Number must be more than 0")
m = 0
arr = []
for i in range(n):
    arr.append(int(input(f"Number {i + 1}: ")))
    if arr[i] > m:
        m = arr[i]
print(f"Max: {m}")
