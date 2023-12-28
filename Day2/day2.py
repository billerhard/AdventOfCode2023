"""
Figure out possible games and add them up
"""

with open("Day2\\input", "r", encoding="utf-8") as inputfile:
    sumgames = 0
    cubetypes = {"red": 12, "green": 13, "blue": 14}

    for line in inputfile:
        validgame=True
        gameno, hands = line.split(":")
        gameno = gameno.strip()
        hands = hands.strip().split(";")
        print(gameno)
        for hand in hands:
            if not validgame:
                break
            cubes = hand.strip().split(",")
            # print("new hand")
            for cube in cubes:
                if not validgame:
                    break
                number, cubetype = cube.strip().split(" ")
                # print("new cube values")
                # print(number)
                # print(cubetype)
                validgame = int(number) <= cubetypes[cubetype]
                print(f"Is {number} a valid number? It should be less than {cubetypes[cubetype]}.")
                # print(f"{validgame}")
        sumgames+= int(gameno.split(" ")[1].strip()) if validgame else 0
        print(sumgames)
