s = sorted(
    frozenset(str(input("Sentence: "))
        .replace(',', "")
        .replace('.', "")
        .replace('?', "")
        .replace('!', "")
        .split())
    )
print("Count:", len(s), "\nSet:", s)
