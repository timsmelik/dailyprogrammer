"""
Challenge #369 (easy)from /r/dailyprogrammer
https://old.reddit.com/r/dailyprogrammer/comments/a0lhxx/20181126_challenge_369_easy_hex_colors/
"""

def hexcolor1(red, green, blue):
    """Most straightforward solution"""
    return '#{:02x}{:02x}{:02x}'.format(red, green, blue)

def hexcolor2(*vals):
    """Use arbitrary number of arguments. Not useful in practice, but fun"""
    return ('#' + '{:02x}' * len(vals)).format(*vals)

#One-liner
hexcolor3 = lambda r, g, b : '#{:02x}{:02x}{:02x}'.format(r, g, b)

hexcolor = hexcolor1

TEST_INPUT = [
    hexcolor(255, 99, 71),
    hexcolor(184, 134, 11),
    hexcolor(189, 183, 107),
    hexcolor(0, 0, 205)
]

print(TEST_INPUT)
