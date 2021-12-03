def rating(oxi, ox_inp, rev):
    for i in range(len(oxi) + 1):
        if len(ox_inp) == 1:
            return int(ox_inp[0], 2)
        is_one = oxi[i].count("1") >= oxi[i].count("0")
        de = set()
        for k, j in enumerate(ox_inp):
            if (j[i] == rev) is is_one:
                de.add(k)
        for k in sorted(de, reverse=True):
            del ox_inp[k]
            for li in oxi:
                del li[k]


if __name__ == "__main__":
    with open("input3.txt", "r") as f:
        inp = [i.removesuffix("\n") for i in f.readlines()]
    inp2 = inp[:]
    ox = []
    for i in range(len(inp[0])):
        ox.append([i for i in map(lambda j: j[i], (j for j in inp))])
    co = [o.copy() for o in ox]
    print(rating(ox, inp, "0") * rating(co, inp2, "1"))
