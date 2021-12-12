def paths(location, been):
    if location == "end":
        global out
        out += 1
        return
    if location.islower():
        been.add(location)
    for place in dic[location]:
        if place not in been:
            paths(place, been.copy())
    return


if __name__ == "__main__":
    dic = {}
    with open("input12.txt", "r") as f:
        for line in f:
            sp = line.removesuffix("\n").split("-")
            for i in range(2):
                try:
                    dic[sp[i]].add(sp[i-1])
                except KeyError:
                    dic[sp[i]] = {sp[i-1]}
    out = 0
    paths("start", set())
    print(out)
