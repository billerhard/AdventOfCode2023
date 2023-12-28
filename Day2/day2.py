"""
Figure out possible games and add them up
"""

with open("Day2\\input", "r", encoding="utf-8") as inputfile:
    sumgames = 0

    for line in inputfile:
        cubetypes = {"red": 0, "green": 0, "blue": 0}
        gameno, hands = line.split(":")
        gameno = gameno.strip()
        hands = hands.strip().split(";")
        for hand in hands:
            cubes = hand.strip().split(",")
            for cube in cubes:
                number, cubetype = cube.strip().split(" ")
                if int(number) >= cubetypes[cubetype]:
                    cubetypes[cubetype] = max(int(number), cubetypes[cubetype])
        sumgames += cubetypes["red"] * cubetypes["green"] * cubetypes["blue"]
    print(sumgames)
