"""
Challenge #366 (easy)from /r/dailyprogrammer
https://old.reddit.com/r/dailyprogrammer/comments/98ufvz/20180820_challenge_366_easy_word_funnel_1/

Given two strings of letters, determine whether the second can be made from
the first by removing one letter. The remaining letters must stay in the same
order.

-- Examples

funnel("leave", "eave")
funnel("reset", "rest")
funnel("dragoon", "dragon")
funnel("eave", "leave") == False
funnel("sleet", "lets") == False
funnel("skiff", "ski") == False
"""

def funnel(word1, word2):
    """Check if word2 can be created by dropping a single character from
    word1. Uses a generator so no unneeded words are generated
    """

    return word2 in (word1[0:i] + word1[i+1:]
                     for i
                     in range(0, len(word1))
                    )

def test():
    """Check if the solution gives the same output as the examples provided
    """

    assert funnel("leave", "eave")
    assert funnel("reset", "rest")
    assert funnel("dragoon", "dragon")
    assert not funnel("eave", "leave")
    assert not funnel("sleet", "lets")
    assert not funnel("skiff", "ski")

if __name__ == '__main__':
    test()
