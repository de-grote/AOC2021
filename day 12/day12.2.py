def paths(location, been, been_once, two):
    if location == "end":
        global out
        out += 1
        return
    if location.islower():
        if location in been_once or two:
            been.add(location)
            two = True
            been = been.union(been_once)
        else:
            been_once.add(location)
    for place in dic[location]:
        if place not in been:
            paths(place, been.copy(), been_once.copy(), two)
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
    paths("start", {"start"}, set(), False)
    print(out)
