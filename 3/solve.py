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

with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        split = int(len(line) / 2)
        left_compartment = line[:split]
        right_compartment = line[split:]

        shared = str(set(left_compartment).intersection(set(right_compartment)))
        priority_sum = priority_sum + char_value(shared)

    print(f"The sum of the priorities is: {priority_sum}")
