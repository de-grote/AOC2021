if __name__ == "__main__":
    with open("input11.txt", "r") as f:
        f = f.readlines()
        inp = [int(j[k]) for j in (list(i.removesuffix("\n")) for i in f) for k in range(len(j))]
        le = len(f[0]) - 1
    out = 0
    for _ in range(100):
        exploded = set()
        while 9 in inp:
            exploded.add((ind := inp.index(9)))
            if not ind % le:
                t = (-le, -le + 1, 1, le, le + 1)
            elif ind % le == le - 1:
                t = (-le - 1, -le, -1, le - 1, le)
            else:
                t = (-le - 1, -le, -le + 1, -1, 1, le - 1, le, le + 1)
            for i in t:
                try:
                    if ind + i < 0:
                        raise IndexError
                    inp[ind + i] += 1 if inp[ind + i] < 9 else 0
                except IndexError:
                    pass
            inp[ind] = -1
        for i, j in enumerate(inp):
            inp[i] = j + 1
        out += len(exploded)
        for i in exploded:
            inp[i] = 0
    print(out)
