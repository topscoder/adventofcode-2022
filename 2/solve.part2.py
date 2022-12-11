#!/usr/bin/env python3

"""
Following the Elf's instructions for the second column, what would your total score be
if everything goes exactly according to your strategy guide?

The total score is still calculated in the same way, but now you need to figure out
what shape to choose so the round ends as indicated.

The example above now goes like this:

    In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.
    In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
    In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.

Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.
"""

their_options = {
    "A": 1,  # Rock
    "B": 2,  # Paper
    "C": 3,  # Scissors
}


def score(he, we) -> int:
    """ Scoring according to strategy guide """
    score = we
    if he == we:
        score = score + 3  # because draw

    elif he == 1 and we == 2:
        score = score + 6  # because won

    elif he == 2 and we == 3:
        score = score + 6  # because won

    elif he == 3 and we == 1:
        score = score + 6  # because won

    else:
        score = score + 0  # because lost

    return score


def decrypt_input(outcome) -> int:
    if outcome == "X":
        return -1  # lose
    elif outcome == "Y":
        return 0  # draw
    elif outcome == "Z":
        return 1  # win


def determine_answer(he, we_should) -> int:
    if we_should == 0:  # we need to draw
        return he

    if we_should == 1:  # we need to win
        return 1 if he + 1 == 4 else he + 1

    if we_should == -1:  # we need to lose
        return 3 if he - 1 == 0 else he - 1


with open("input.txt", "r") as f:
    total_score = 0
    for line in f:
        game = line.strip().split(" ")
        he = their_options[game[0]]
        we_should = decrypt_input(game[1])
        we = determine_answer(he, we_should)
        scored = score(he, we)
        print(f"{he} vs {we} = {scored}")
        total_score = total_score + scored

    print(f"Total score = {total_score}")
