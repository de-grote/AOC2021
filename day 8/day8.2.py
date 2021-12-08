if __name__ == "__main__":
    with open("input8.txt", "r") as f:
        inp = [i.removesuffix("\n").split(" | ") for i in f.readlines()]
    out = 0
    for a in inp:
        pos = [[chr(j + 97) for j in range(7)] for _ in range(7)]
        for b in a[0].split(" "):
            for c in b:
                if len(b) == 2:
                    cas = 2, 5
                elif len(b) == 3:
                    cas = 0, 2, 5
                elif len(b) == 4:
                    cas = 1, 2, 3, 5
                else:
                    continue
                for i in range(7):
                    if all(ca != i for ca in cas):
                        if c in pos[i]:
                            pos[i].remove(c)
                    else:
                        for j in pos[i]:
                            if j not in b:
                                pos[i].remove(j)
        temp = []
        for b in a[1].split(" "):
            match len(b):
                case 2:
                    temp.append("1")
                case 3:
                    temp.append("7")
                case 4:
                    temp.append("4")
                case 5:
                    t = [p[:] for p in pos]
                    for j in t:
                        for i in j:
                            if i not in b:
                                j.remove(i)
                    for k in 3, 6:
                        if len(t[k]) == 1 and t.count(t[k]) >= 2:
                            for i, j in enumerate(t):
                                if i != k and j == t[k]:
                                    t[i] = []
                    if t[1]:
                        temp.append("5")
                    else:
                        if t[4]:
                            temp.append("2")
                        else:
                            temp.append("3")
                case 6:
                    t = [p[:] for p in pos]
                    for j in t:
                        for i in j:
                            if i not in b:
                                j.remove(i)
                    for k in 5, 6:
                        if len(t[k]) == 1 and t.count(t[k]) >= 2:
                            for i, j in enumerate(t):
                                if i != k and j == t[k]:
                                    t[i] = []
                    if not t[4]:
                        temp.append("9")
                    elif not t[2]:
                        temp.append("6")
                    else:
                        temp.append("0")
                case 7:
                    temp.append("8")
        out += int("".join(temp))
    print(out)
