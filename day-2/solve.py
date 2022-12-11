#!/usr/bin/env python3

"""
What would your total score be if everything goes exactly
according to your strategy guide?

This strategy guide predicts and recommends the following:

    In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
    In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
    The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.

In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).
"""

our_options = {
    "X": 1,  # Rock
    "Y": 2,  # Paper
    "Z": 3,  # Scissors
}

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


with open("input.txt", "r") as f:
    total_score = 0
    for line in f:
        game = line.strip().split(" ")
        he = their_options[game[0]]
        we = our_options[game[1]]
        scored = score(he, we)
        print(f"{he} vs {we} = {scored}")
        total_score = total_score + scored

    print(f"Total score = {total_score}")
