"""
Challenge #363 (easy)from /r/dailyprogrammer, Regex version
https://old.reddit.com/r/dailyprogrammer/comments/8q96da/20180611_challenge_363_easy_i_before_e_except/
"""

import re

# Added madeup word "beicei" to check for multiple occurences of "ei" combinations
WORDS = [
    "a",
    "zombie",
    "transceiver",
    "veil",
    "icier",
    "beicei"
]

def check(word):
    """Checks if the word follows the "I before E except after C" rule. If
    the word contains "cie" it does not follow the rule. If the word contains
    an occurence of "ei" at the start of the string or not following a 
    character other than c, it does not follow the rule.

    Positional arguments:
    word -- the word to check
    """

    return re.search('cie|[^c]ei|^ei', word) is None

for w in WORDS:
    print(check(w))
