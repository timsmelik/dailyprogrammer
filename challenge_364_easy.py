"""
Challenge #364 (easy)from /r/dailyprogrammer
https://old.reddit.com/r/dailyprogrammer/comments/8s0cy1/20180618_challenge_364_easy_create_a_dice_roller/
"""

from random import randrange

ROLLS = [
    "5d12",
    "6d4",
    "1d2",
    "1d8",
    "3d6",
    "4d20",
    "100d100"
]

def roll_dice(roll: str) -> int:
    """Return the total value of the role based on the number of dice and the number of sides

    Positional arguments
    roll -- a string consisting of the number of dice, followed by a "d"
        and then the number of sides the dice have
    """
    n_dice, n_sides = (int(x) for x in roll.split("d"))
    return sum(randrange(0, n_sides) for _ in range(0, n_dice))

for r in ROLLS:
    print(roll_dice(r))
