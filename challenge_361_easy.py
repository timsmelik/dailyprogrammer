"""
Challenge #361 (easy)from /r/dailyprogrammer
https://old.reddit.com/r/dailyprogrammer/comments/8jcffg/20180514_challenge_361_easy_tally_program/
"""

from collections import namedtuple
from operator import attrgetter

CHALLENGE_INPUT = [
    "abcde",
    "dbbaCEDbdAacCEAadcB"
]

Player = namedtuple('Player', ['name', 'score'])

def calculate_total_scores(scores):
    """Calculate totals of all players present in the scorelist. Each player
    is represented by a single character. Lowercase characters award a point
    to the player, uppercase characters take away a point from the player.
    A player is assumed to take part in the game when their character,
    either as lowercase or uppercase, is found at least once in the scores.

    The list is sorted by score, descending.
    """

    players = set(scores.lower())

    return sorted([
        Player(name=k, score=scores.count(k) - scores.count(k.upper()))
        for k in players
    ], key=attrgetter('score'), reverse=True)

def print_for_challenge(score_list):
    """Print the list of players according to the challenge specifications"""
    print(', '.join(f'{player.name}:{player.score}' for player in score_list))

for ci in CHALLENGE_INPUT:
    total_scores = calculate_total_scores(ci)
    print_for_challenge(total_scores)
