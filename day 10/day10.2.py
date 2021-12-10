if __name__ == "__main__":
    with open("input10.txt", "r") as f:
        inp = [i.removesuffix("\n") for i in f.readlines()]
    stack, err, out = [], [], []
    opening = "([{<"
    closing = ")]}>"
    for i in inp:
        for j in i:
            if j in opening:
                stack.append(j)
            elif opening[closing.index(j)] == stack[-1]:
                stack.pop()
            else:
                stack.clear()
                break
        if stack:
            err.append("".join(stack))
        stack.clear()
    for e in err:
        temp = 0
        for f in range(1, len(e) + 1):
            temp *= 5
            temp += opening.index(e[-f]) + 1
        out.append(temp)
    out.sort()
    print(out[len(out) // 2])
