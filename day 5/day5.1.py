if __name__ == "__main__":
    with open("input5test.txt", "r") as f:
        coordinates = [",".join(i.removesuffix("\n").split(" -> ")).split(",") for i in f.readlines()]
    row = [0 for _ in range(1000)]
    board = [row[:] for _ in range(1000)]
    for i in coordinates:
        if i[1] == i[3] or i[0] == i[2]:
            for j in range(min(int(i[0]), int(i[2])), max(int(i[0]), int(i[2])) + 1):
                for k in range(min(int(i[1]), int(i[3])), max(int(i[1]), int(i[3])) + 1):
                    board[k][j] += 1
    out = 0
    for r in board:
        out += sum(i >= 2 for i in r)
    print(out)
