inp = str(input("Letters: "))
d = dict()
for letter in inp:
	if letter in d:
		d[letter] += 1 
	else:
		d[letter] = 1
print(d)
