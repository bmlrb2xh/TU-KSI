arr = list()
while True:
    num = float(input(f"Number {len(arr) + 1}: "))
    if num == -99:
        break
    arr.append(num)
arr = list(filter(lambda num: num > 0, arr))
prod = 1
for num in arr:
    prod = prod * num
print("Sum:", sum(arr), "\nProduct:", prod)
