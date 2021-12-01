if __name__ == "__main__":
    with open("input1.txt", "r") as f:
        inp = [int(i.removesuffix("\n")) for i in f.readlines()]
    out = 0
    for i, j in enumerate(inp):
        out += j > inp[i-1] if i else 0
    print(out)
