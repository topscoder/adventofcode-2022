#!/usr/bin/env python3

elves = []
calories = 0

with open("input.txt", "r") as f:
    for x in f:
        if x.strip() == "":
            elves.append(calories)
            calories = 0
            continue

        calories = calories + int(x.strip())

print(f"The answer is: {max(elves)}")
