"""
Challenge #363 (easy)from /r/dailyprogrammer
https://old.reddit.com/r/dailyprogrammer/comments/8q96da/20180611_challenge_363_easy_i_before_e_except/
"""

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
    more occurences of "ei" than "cei", at least one of those occurences does
    not follow a "c" and thus the word does not follow the rulei

    Positional arguments:
    word -- the word to check
    """

    return not "cie" in word and word.count("ei") == word.count("cei")

for w in WORDS:
    print(check(w))
