if __name__ == "__main__":
    with open("input17.txt", "r") as f:
        inp = tuple(int(j) for i in f.readline()[15:].split(", y=") for j in i.split(".."))
    max_y = -min(inp[2:]) - 1
    min_y = min(inp[2:])
    max_x = max(inp[:2])
    min_x = int((min(inp[:2]) * 2) ** 0.5)
    out = 0
    for i in range(min_x, max_x + 1):
        for j in range(min_y, max_y + 1):
            loc = [0, 0]
            x, y = i, j
            while max(inp[:2]) >= loc[0] and loc[1] >= min(inp[2:]):
                loc[0] += x
                loc[1] += y
                y -= 1
                if x:
                    x -= 1
                if loc[0] in range(min(inp[:2]), max(inp[:2]) + 1) and loc[1] in range(min(inp[2:]), max(inp[2:]) + 1):
                    out += 1
                    break
    print(out)
