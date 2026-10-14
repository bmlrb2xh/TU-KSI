n = int(input("Number: "))
if n <= 1:
    print("Not a prime number")
else:
    prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            prime = False
            break
    print("Prime number" if prime else "Not a prime number")
