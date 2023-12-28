"""
add up some part numbers
"""
import re

arr = [[0 for i in range(141)] for j in range(140)]


def check_pos(start, end):
    """
    find symbols near pos
    """
    for x in range(max(start[0] - 1,0), min(end[0] + 2, 139)):
        for y in range(max(start[1] - 1,0), min(end[1] + 2, 139)):
            print(x, y, arr[x][y])
            character=arr[x][y]
            if re.search(r"[^\.\d\n]", str(arr[x][y])):
                print(f"found symbol near number: {arr[x][y]}")
                return True
    # print("did not find symbol")
    return False


def get_num(start, end):
    """
    turn numbers into strings of numbers
    """
    strnum = ""
    for x in range(start[0], end[0] + 1):
        for y in range(start[1], end[1]):
            strnum = strnum + arr[x][y]

    return strnum


with open("Day3\\input", "r", encoding="utf-8") as inputfile:
    startpos = endpos = x, y = 0, 0
    readingnumber = False
    sumnum = 0
    for line in inputfile:
        for character in line:
            arr[x][y] = character
            y += 1
        x += 1
        y = 0
    x,y=0,0
    for line in arr[x]:
        for character in line[y]:
            match = re.search(r"\d", character)
            if readingnumber:
                if match:
                    pass
                else:
                    endpos = x, y
                    readingnumber = False
                    # print(f"number: {get_num(startpos, endpos)}")
                    addnum = check_pos(startpos, endpos)

                    if addnum:
                        sumnum += int(get_num(startpos, endpos))

            else:
                if match:
                    startpos = x, y
                    readingnumber = True
            y += 1
        x += 1
        y = 0
print(sumnum)
