s = list(str(input("String: ")).replace(' ', ""))
d = dict()
for ch in s:
	if ch in d:
		d[ch] += 1
	else:
		d[ch] = 1
char = ""
count = 0
for key, value in d.items():
	if value > count:
		count = value
		char = key
print("Symbol:", char, "\nCount:", count)
