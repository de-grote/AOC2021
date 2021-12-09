if __name__ == "__main__":
    with open("input9.txt", "r") as f:
        h_map = [j for j in (list(i.removesuffix("\n")) for i in f.readlines())]
    for j, h in enumerate(h_map):
        h_map[j] = [i != "9" for i in h]
    coordinates = [(i, j) for i in range(len(h_map[0])) for j in range(len(h_map))]
    todo = set()
    out = []
    while coordinates:
        x, y = coordinates[0]
        if h_map[y][x]:
            basin = 0
            todo.add((x, y))
            while todo:
                x, y = todo.pop()
                for i, j in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    try:
                        if y+i < 0 or x+j < 0:
                            raise IndexError
                        if h_map[y+i][x+j]:
                            if (x+j, y+i) in coordinates:
                                todo.add((x+j, y+i))
                        else:
                            del coordinates[coordinates.index((x+j, y+i))]
                    except (IndexError, ValueError):
                        pass
                basin += 1
                del coordinates[coordinates.index((x, y))]
            out.append(basin)
        else:
            del coordinates[0]
    o1 = max(out)
    out.remove(o1)
    o2 = max(out)
    out.remove(o2)
    print(max(out) * o1 * o2)
