"""
Challenge #369 (easy)from /r/dailyprogrammer
https://old.reddit.com/r/dailyprogrammer/comments/a0lhxx/20181126_challenge_369_easy_hex_colors/
"""

from functools import reduce

def hexcolor1(red, green, blue):
    """Most straightforward solution"""
    return '#{:02x}{:02x}{:02x}'.format(red, green, blue)

# Fun/bonus solutions below, not very useful

def hexcolor2(*vals):
    """Use arbitrary number of arguments"""
    return ('#' + '{:02x}' * len(vals)).format(*vals)

#One-liner
hexcolor3 = lambda r, g, b : '#{:02x}{:02x}{:02x}'.format(r, g, b)

def hexcolor4(r, g, b):
    """Use map"""
    return '#' + ''.join(map(lambda x : '{:02x}'.format(x), (r, g, b)))

def hexcolor5(r, g, b):
    """Use reduce"""
    return reduce(lambda a, b : a + '{:02x}'.format(b), ('#', r, g, b))

hexcolor = hexcolor5

TEST_INPUT = [
    hexcolor(255, 99, 71),
    hexcolor(184, 134, 11),
    hexcolor(189, 183, 107),
    hexcolor(0, 0, 205)
]

print(TEST_INPUT)
