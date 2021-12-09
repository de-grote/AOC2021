if __name__ == "__main__":
    with open("input9.txt", "r") as f:
        h_map = [j for j in (list(i.removesuffix("\n")) for i in f.readlines())]
    temp = []
    out = 0
    for y, row in enumerate(h_map):
        for x, v in enumerate(row):
            for i, j in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                try:
                    if y+i < 0 or x+j < 0:
                        raise IndexError
                    temp.append(h_map[y+i][x+j])
                except IndexError:
                    pass
            if min(int(t) for t in temp) > int(v):
                out += int(v) + 1
            temp.clear()
    print(out)
