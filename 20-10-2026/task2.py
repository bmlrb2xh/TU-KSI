import random

li = list()
n = 10
for i in range(n):
	li.append(random.randint(0, 100))
print("List:", li)
# j = 0
# for i in range(n - 1):
# 	li.insert(i + 1+ j, li[i + j] + li[i + 1 + j])
# 	j += 1
li2 = list()
for i in range(n - 1):
	li2.append(li[i])
	li2.append(li[i] + li[i + 1])
li2.append(li[n - 1])
print("Changed list:", li2)
