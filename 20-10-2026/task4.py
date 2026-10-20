num = int(input("Number: "))
li = list(range(1, num + 1))
res = dict()
for n in li:
	res[n] = li[num - 1]
	num -= 1
print(li)
print(res)
