n = 0
while True:
    n = int(input("Number: "))
    if n >= 1 and n <= 7:
        break
    print("Number must be in the range [1-7]")
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(f"Day {n}: {weekdays[n - 1]}")
