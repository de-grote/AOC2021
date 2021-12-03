if __name__ == "__main__":
    with open("input3.txt", "r") as f:
        inp = [i.removesuffix("\n") for i in f.readlines()]
    length = len(inp) // 2
    gamma = []
    for i in range(len(inp[0])):
        gamma.append("".join(i for i in map(lambda j: j[i], (j for j in inp))).count("1") > length)
    print(int("".join(str(int(g)) for g in gamma), 2) * int("".join(str(int(not g)) for g in gamma), 2))
