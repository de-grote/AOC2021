if __name__ == "__main__":
    coordinates = set()
    with open("input13.txt", "r") as f:
        for line in f:
            if line == "\n":
                break
            coordinates.add(tuple(int(i) for i in line.removesuffix("\n").split(",")))
        fold = f.readline()
    if fold[11] == "y":
        check = (0, int(fold[13:]))
    else:
        check = (int(fold[13:]), 0)
    new = set()
    for c in coordinates:
        new.add((abs(check[0] - c[0]), abs(check[1] - c[1])))
    print(len(new), new)
