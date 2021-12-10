if __name__ == "__main__":
    with open("input10.txt", "r") as f:
        inp = [i.removesuffix("\n") for i in f.readlines()]
    stack, err = [], []
    opening = "([{<"
    closing = ")]}>"
    for i in inp:
        for j in i:
            if j in opening:
                stack.append(j)
            elif opening[closing.index(j)] == stack[-1]:
                stack.pop()
            else:
                err.append(j)
                stack.clear()
                break
    print(err.count(")")*3+err.count("]")*57+err.count("}")*1197+err.count(">")*25137)
