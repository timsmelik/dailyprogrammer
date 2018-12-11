"""
Challenge #359 (easy)from /r/dailyprogrammer
https://old.reddit.com/r/dailyprogrammer/comments/8g0iil/20180430_challenge_359_easy_regular_paperfold/
"""

TEST_OUTPUT = '1101100111001001110110001100100111011001110010001101100011001001110110011100100111011000110010001101100111001000110110001100100111011001110010011101100011001001110110011100100011011000110010001101100111001001110110001100100011011001110010001101100011001001110110011100100111011000110010011101100111001000110110001100100111011001110010011101100011001000110110011100100011011000110010001101100111001001110110001100100111011001110010001101100011001000110110011100100111011000110010001101100111001000110110001100100'

def paperfold(s):
    """Insert alternating 1's and 0's in front, between and after every 
    character of the input string
    """

    return '1' + ''.join(s[i] + str(i % 2) for i in range(0, len(s)))

def paperfold_n_times(s, n):
    if n == 1:
        return paperfold(s)
    else:
        return paperfold_n_times(paperfold(s), n - 1)

def test():
    challenge_input = '1'
    
    challenge_output = challenge_input

    for _ in range(8):
        challenge_output = paperfold(challenge_output)

    assert challenge_output == TEST_OUTPUT

    assert paperfold_n_times(challenge_input, 8) == TEST_OUTPUT

test()
