def bingo():
    global last_number
    last_del = []
    for d in draw:
        de = set()
        d = str(d)
        for board in boards:
            for row in board:
                if d in row:
                    row[row.index(d)] = ""
                if row.count("") == 5:
                    de.add(boards.index(board))
            for i in range(len(board)):
                if all(not board[j][i] for j in range(len(board))):
                    de.add(boards.index(board))
        for delete in sorted(de, reverse=True):
            last_del = boards[delete][:]
            del boards[delete]
        if len(boards) == 0:
            last_number = int(d)
            return last_del
        de.clear()


if __name__ == "__main__":
    with open("input4.txt", "r") as f:
        f = f.readlines()
        draw = [int(i) for i in f[0].removesuffix("\n").split(",")]
        board = [j.removesuffix("\n").replace("  ", " ").split(" ") for j in f[2:]]
    boards = []
    temp = []
    for b in board:
        while "" in b:
            b.remove("")
        if b:
            temp.append(b)
        else:
            boards.append(temp)
            del temp
            temp = []
    boards.append(temp)
    out = 0
    last_number = 0
    for i in bingo():
        out += sum(int(j) if j else 0 for j in i)
    print(out * last_number)
