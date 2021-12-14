if __name__ == "__main__":
    letters = set()
    replace = {}
    with open("input14.txt", "r") as f:
        start = f.readline().removesuffix("\n")
        end = start[-1]
        for line in f.readlines()[1:]:
            replace.update({line[0:2]: line[6]})
            for i in (0, 1, 6):
                letters.add(line[i])
    inp = {}
    for key in replace:
        inp.update({key: 0})
    for c, _ in enumerate(start):
        if len(start[c:c+2]) == 2:
            inp[start[c:c+2]] += 1
    for _ in range(40):
        new = {}
        for key in replace:
            new.update({key: 0})
        for i in inp:
            new[i[0]+replace[i]] += inp[i]
            new[replace[i]+i[1]] += inp[i]
        inp = new
    out = set()
    for letter in letters:
        temp = 0
        for i in inp:
            if letter in i:
                if letter == i[0] and letter == i[1]:
                    temp += inp[i]
                else:
                    temp += inp[i] // 2 + (i == end)
        out.add(temp)
    print(max(out) - min(out))
