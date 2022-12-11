

""" In how many assignment pairs does one range fully contain the other? """


def contained(range1, range2) -> bool:
    "6-6, 4-6"
    range1 = range1.split('-')
    range1[0] = int(range1[0])
    range1[1] = int(range1[1])

    range2 = range2.split('-')
    range2[0] = int(range2[0])
    range2[1] = int(range2[1])

    if range1[0] >= range2[0] and range1[1] <= range2[1]:
        return True

    "4-6, 4-4"
    if range2[0] >= range1[0] and range2[1] <= range1[1]:
        return True

    return False


contained_pairs = 0

with open("input.txt", "r") as f:
    content_lines = f.read().split("\n")
    for line in content_lines:
        pairs = line.split(",")
        if contained(pairs[0], pairs[1]):
            contained_pairs = contained_pairs + 1

    print(f"In how many assignment pairs does one range fully contain the other? {contained_pairs}")
