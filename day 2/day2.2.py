if __name__ == "__main__":
    with open("input2.txt", "r") as f:
        inp = [i.removesuffix("\n") for i in f.readlines()]
    horizontal = 0
    depth = 0
    aim = 0
    for i in inp:
        num = int(i.split(" ")[-1])
        match i[0]:
            case "f":
                horizontal += num
                depth += num * aim
            case "d":
                aim += num
            case "u":
                aim -= num
    print(horizontal * depth)
