if __name__ == "__main__":
    letters = set()
    replace = {}
    with open("input14.txt", "r") as f:
        start = f.readline().removesuffix("\n")
        for line in f.readlines()[1:]:
            replace.update({line[0:2]: line[6]})
            for i in (0, 1, 6):
                letters.add(line[i])
    for letter in letters:
        replace.update({letter: ""})
    for test in range(10):
        start = "".join(start[i]+j for i, j in enumerate(replace[start[k:k+2]] for k, _ in enumerate(start)))
    out = [start.count(letter) for letter in letters]
    print(max(out) - min(out))
