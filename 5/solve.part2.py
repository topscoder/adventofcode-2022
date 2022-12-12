import math
import re

# Parse stacks
stacks = []
instructions = []
nr_stacks = 0

is_header = True
is_instruction = False

with open('input.txt') as f:
    lines = f.read().split("\n")

    for line in lines:
        if line.strip() == "":
            is_header = False
            is_instruction = True
            continue

        if is_header:
            stacks.append(line)

        if is_instruction:
            instructions.append(line)


def parse_stack_lines(stack_lines):
    stacks = []

    line_stack_numbers = stack_lines.pop()
    nr_stacks = math.ceil(len(line_stack_numbers) / 4)

    print(f"The amount of stacks is: {nr_stacks}")

    # Init stacks list with empty items for amount of stacks
    i = 0
    while i < nr_stacks:
        # if i not in stacks:
        stacks.append([])
        i = i + 1

    for line in stack_lines:
        stacks = parse_stack_line(line, stacks)

    return stacks


def parse_stack_line(line, stacks):
    if len(line) == 0:
        return stacks

    length = len(line)
    stack_amount = math.ceil(length / 4)

    colsize = 3
    sepsize = 1

    col = 0
    while col < stack_amount:
        # col is either
        # -   (3 spaces)
        # - [X] (character between brackets)
        # -  0 (space number space)
        pos0 = 0 + (col * colsize) + (col * sepsize)
        pos1 = 1 + (col * colsize) + (col * sepsize)
        pos2 = 2 + (col * colsize) + (col * sepsize)

        if line[pos0] == "[":
            stacks[col].append(line[pos1:pos2])

        if line[pos0] == " " and line[pos1] != " ":
            stacks[col].append(line[pos1:pos2])

        col = col + 1

    return stacks


stacks = parse_stack_lines(stacks)
print(stacks)

# Parse instructions
for instruction_line in instructions:
    if len(instruction_line.strip()) == 0:
        continue

    print("")
    print(instruction_line)

    # move {amount} from {source} to {target}
    matches = re.findall(
        r'^move ([\d]+) from ([\d]) to ([\d])', instruction_line)
    amount = int(matches[0][0])
    source = int(matches[0][1])
    target = int(matches[0][2])

    # The pop() method removes the item at the given index from the list and returns the removed item.
    if amount > len(stacks[source - 1]):
        print(
            f"Looks like we are bugging because moving {amount} from stack {stacks[source - 1]} seems impossible.")
        exit(1)

    move = stacks[source - 1][0:amount]
    print(f"moving: {move}")
    del stacks[source - 1][0:amount]
    # move.reverse()
    stacks[target - 1] = move + stacks[target - 1]

answer = ""
for stack in stacks:
    if len(stack) > 0:
        answer = answer + stack[0:1].pop()

print(
    f"After the rearrangement procedure completes, what crate ends up on top of each stack? {answer}")
