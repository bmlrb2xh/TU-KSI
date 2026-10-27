s = list(str(input("Space seperated list of strings: ")).split())
k = int(input("k: "))
res = tuple(filter(lambda word: len(word) >= k, s))
print(res)
