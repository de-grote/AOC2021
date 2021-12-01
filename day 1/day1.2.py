if __name__ == "__main__":
    with open("input1.txt", "r") as f:
        inp = [int(i.removesuffix("\n")) for i in f.readlines()]
    out = 0
    old = 0
    for i in range(len(inp) + 1):
        new = sum(inp[i-3:i])
        if new > old != 0:
            out += 1
        old = new
    print(out)
