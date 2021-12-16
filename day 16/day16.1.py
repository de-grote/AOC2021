def lit_val(val):
    global out
    out += int(val[0:3], 2)
    break_on_next = False
    loops = 0
    for i, b in enumerate(val[6:]):
        if not i % 5:
            if break_on_next:
                break
            loops += 1
            break_on_next = not int(b)
    return val[6 + loops * 5:]


def package(val):
    global out
    out += int(val[0:3], 2)
    if int(val[6]):
        i = int(val[7:18], 2)
        val = val[18:]
        extra = ""
    else:
        i = int(val[7:22], 2)
        extra = val[22+i:]
        val = val[22:22+i]
    for j in range(i):
        if val:
            if val[3:6] == "100":
                val = lit_val(val)
            else:
                val = package(val)
        else:
            break
    return val + extra


if __name__ == "__main__":
    with open("input16.txt", "r") as f:
        inp = f.readline()
    inp = "".join("0" for i in range(len(bin(int(inp, 16))[2:]) % -4 * -1)) + bin(int(inp, 16))[2:]
    out = 0
    if inp[3:6] == "100":
        lit_val(inp)
    else:
        package(inp)
    print(out)
