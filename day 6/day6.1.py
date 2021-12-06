if __name__ == "__main__":
    with open("input6.txt", "r") as f:
        fish = [int(i) for i in f.readline().split(",")]
    for t in range(80):
        fish = [f - 1 if f else 8 for f in fish]
        fish.extend((6 for _ in range(fish.count(8))))
    print(len(fish))
