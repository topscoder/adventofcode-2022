#!/usr/bin/env python3

import string

"""

a-z = 1-26
A-Z = 27-52

"""


def char_value(input_str) -> int:
    character_values = list(string.ascii_lowercase) + \
        list(string.ascii_uppercase)

    input_str = input_str[2]  # '{a}'

    i = 0
    for el in character_values:
        if el == input_str:
            return i + 1

        i = i + 1

    return 0


priority_sum = 0

with open("input.part2.txt", "r") as f:
    # Every 3 lines represent a group
    file_contents = f.read().split("\n")

    num_groups = int(len(file_contents) / 3)

    for grp in range(0, num_groups):
        set1 = set(file_contents[grp*3+0])
        set2 = set(file_contents[grp*3+1])
        set3 = set(file_contents[grp*3+2])
        prio = set.intersection(set1, set2, set3)
        priority_sum = priority_sum + char_value(str(prio))

    print(f"The sum of the priorities is: {priority_sum}")
