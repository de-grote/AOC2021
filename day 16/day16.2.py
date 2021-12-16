def lit_val(val):
    break_on_next = False
    num = []
    loops = 0
    for i, b in enumerate(val[6:]):
        if not i % 5:
            if break_on_next:
                break
            loops += 1
            break_on_next = not int(b)
        else:
            num.append(b)
    return val[6 + loops * 5:], int("".join(num), 2)


def package(val):
    Type = val[3:6]
    if int(val[6]):
        i = int(val[7:18], 2)
        val = val[18:]
        extra = ""
    else:
        i = int(val[7:22], 2)
        extra = val[22+i:]
        val = val[22:22+i]
    nums = []
    for j in range(i):
        if val:
            if val[3:6] == "100":
                val, c = lit_val(val)
            else:
                val, c = package(val)
            nums.append(c)
        else:
            break
    match Type:
        case "000":
            calc = sum(nums)
        case "001":
            t = 1
            for n in nums:
                t *= n
            calc = t
        case "010":
            calc = min(nums)
        case "011":
            calc = max(nums)
        case "101":
            calc = int(nums[0] > nums[1])
        case "110":
            calc = int(nums[0] < nums[1])
        case "111":
            calc = int(nums[0] == nums[1])
    return val + extra, calc


if __name__ == "__main__":
    with open("input16.txt", "r") as f:
        inp = f.readline()
    inp = "".join("0" for i in range(len(bin(int(inp, 16))[2:]) % -4 * -1)) + bin(int(inp, 16))[2:]
    if inp[3:6] == "100":
        _, out = lit_val(inp)
    else:
        _, out = package(inp)
    print(out)
