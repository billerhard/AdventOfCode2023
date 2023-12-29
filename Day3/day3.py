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
            if re.search(r"[^\.\d\n]", str(arr[x][y])):
                print(f"found symbol: {arr[x][y]} near number: {get_num(start, end)}")
                return True
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
def main():
    '''
    main
    '''
    with open("Day3\\input", "r", encoding="utf-8") as inputfile:
        startpos = endpos = x, y = 0, 0
        reading_number = False
        sum_num = 0
        for line in inputfile:
            for character in line:
                arr[x][y] = character
                y += 1
            x += 1
            y = 0
        x,y=0,0
        print(x,y)
    with open("Day3\\input", "r", encoding="utf-8") as inputfile:
        for line in inputfile:
            # print(line)
            for character in line:
                match = re.search(r"\d", arr[x][y])
                if reading_number:
                    if match:
                        pass
                    else:
                        endpos = x, y
                        reading_number = False
                        add_num = check_pos(startpos, endpos)
                        if add_num:
                            sum_num += int(get_num(startpos, endpos))
                            print(sum_num)
                else:
                    if match:
                        startpos = x, y
                        reading_number = True
                y += 1
            x += 1
            y = 0
main()
