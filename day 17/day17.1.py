if __name__ == "__main__":
    with open("input17.txt", "r") as f:
        print((inp := -min(int(i) for i in f.readline().split("y=")[-1].split("..")) - 1) * (inp + 1) // 2)
