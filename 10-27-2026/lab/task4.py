d = dict()
for i in range(3):
    print(f"Person {i + 1}:")
    name = str(input("Name: "))
    d[name] = str(input("Phone number: "))
name = str(input("Name to search: "))
if name in d:
	print(f"The phone number of {name} is:", d[name])
else:
	print("Person not found")
