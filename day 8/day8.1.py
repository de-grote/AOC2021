if __name__ == "__main__":
    with open("input8.txt", "r") as f:
        print([len(i.removesuffix("\n").split("| ")[1].split(" ")[j]) % 7 <= 4
               for i in f.readlines() for j in range(4)].count(True))
