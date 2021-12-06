if __name__ == "__main__":
    with open("input6.txt", "r") as f:
        fish = [int(i) for i in f.readline().split(",")]
    fish0, fish1, fish2, fish3, fish4, fish5, fish6, fish7, fish8 =\
        fish.count(0), fish.count(1), fish.count(2), fish.count(3), fish.count(4), \
        fish.count(5), fish.count(6), fish.count(7), fish.count(8)
    for t in range(256):
        fish0, fish1, fish2, fish3, fish4, fish5, fish6, fish7, fish8 =\
            fish1, fish2, fish3, fish4, fish5, fish6, fish7 + fish0, fish8, fish0
    print(fish0+fish1+fish2+fish3+fish4+fish5+fish6+fish7+fish8)
