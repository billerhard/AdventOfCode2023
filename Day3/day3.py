"""
add up some part numbers
"""
import re

def check_for_symbols(lines, line_number, span):
    '''
    check for symbols near line_number,span in lines
    '''
    line_range=range(max(line_number-1,0),min(line_number+1,140))
    span_range=range(max(span[0]-1,0),min(span[1]+1,140))
    for i in line_range:
        for j in span_range:
            if re.search(r"[^\d\.\n]",lines[i][j]):
                # print(f"found symbol {lines[i][j]} at position {i,j}")
                return True
    return False

def main():
    '''
    main
    '''
    sumnum=0
    with open("Day3\\input", "r", encoding="utf-8") as inputfile:
        lines=inputfile.readlines()
    i=0
    for line in lines:
        matches=re.findall(r"\d+", line)
        for number in matches:
            match=re.search(rf"{number}", line)
            found_symbol=check_for_symbols(lines,i,match.span())
            if found_symbol:
                print(f"adding number: {number} to sum due to found symbol.")
                sumnum+=int(number)

        i+=1
    print(sumnum)
main()
