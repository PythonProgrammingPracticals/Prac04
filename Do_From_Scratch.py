import random

quick_picks = int(input("How many quick picks would you like: "))

for y in range(1, quick_picks+1):
    quick_pick = []
    for x in range (1, 6+1):
        quick_pick.append(random.randrange(1, 45+1, 1))
    while len(quick_pick) > len(set(quick_pick)):
        quick_pick = []
        for z in range (1, 6 + 1):
            quick_pick.append(random.randrange(1, 45 + 1, 1))


    quick_pick = sorted(quick_pick, key=int)
    print(" {:2d} {:2d} {:2d} {:2d} {:2d} {:2d}".format(quick_pick[0], quick_pick[1], quick_pick[2], quick_pick[3],
                                                        quick_pick[4], quick_pick[5]))