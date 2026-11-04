def is_palindrome(number: int):
    opposite = int(str(number)[::-1])
    return 1 if number - opposite == 0 else 0
print(is_palindrome(int(input("Number: "))))
