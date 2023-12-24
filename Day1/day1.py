"""
find some numbers in some words and add them up
"""
import re

with open("Day1\\input", "r", encoding="utf-8") as inputfile:
    SUMVALUES = 0
    WORDS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    REGEX = r"one|two|three|four|five|six|seven|eight|nine|\d"
    for line in inputfile:
        first = re.search(rf"{REGEX}", line)[0]
        last = re.findall(rf"(?=({REGEX}))", line)[-1]
        if first in WORDS:
            first = WORDS.index(first) + 1
        if last in WORDS:
            last = WORDS.index(last) + 1
        SUMVALUES += int(str(first) + str(last))
    print(f"{SUMVALUES}")
