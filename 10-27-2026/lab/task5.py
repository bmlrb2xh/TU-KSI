arr = list(map(int, str(input("List of space separated numbers ([num1] [num2] [num3]...):")).split()))
print("Original list:", arr)
nodupes = list()
for num in arr:
    if num not in nodupes:
        nodupes.append(num)
print("Without duplicates:", nodupes)
