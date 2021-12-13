if __name__ == "__main__":
    coordinates = set()
    with open("input13.txt", "r") as f:
        for line in f:
            if line == "\n":
                break
            coordinates.add(tuple(int(i) for i in line.removesuffix("\n").split(",")))
        fold = f.readlines()
    for inst in fold:
        if inst[11] == "y":
            check = (0, int(inst[13:]))
        else:
            check = (int(inst[13:]), 0)
        new = set()
        for c in coordinates:
            new.add((check[0]-abs(c[0] - check[0]) if check[0] else c[0],
                     check[1]-abs(c[1] - check[1]) if check[1] else c[1]))
        coordinates = new.copy()
    out = [["." for _ in range(max(c[0] for c in coordinates)+1)] for _ in range(max(c[1] for c in coordinates)+1)]
    for c in coordinates:
        out[c[1]][c[0]] = "#"
    for o in out:
        print("".join(o))
