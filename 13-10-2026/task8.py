lo = float(input("Lower limit: "))
hi = float(input("Higher limit: "))
if lo > hi:
    temp = lo
    lo = hi
    hi = temp
num = 0
res = 0
for i in range(10):
    num = float(input(f"Number {i + 1}: "))
    if num > lo and num < hi:
        res += 1
print(f"Amount of numbers in the range [{lo} - {hi}]: {res}")
