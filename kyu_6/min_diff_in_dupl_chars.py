# Task
# Write a function that takes a string and finds a repeating
# character in the string (there may be multiple repeating characters).
# The function should return the minimum difference between the indices
# of these characters and the character itself.
#
# For example, in the string "aabcba", the minimum position
# difference of repeated characters will be equal to 1, since
# for the character "a", the position difference is 1.
#
# The output should be in the form of an array.
#
# If there are no duplicate characters in the string, it should return null.
#
# The string can only contain lowercase letters, and nothing else!!!
# (an empty string is not allowed).
#
# If the difference between repeated characters is the same, return
# the first minimal difference encountered.


def min_repeating_character_difference(text: str) -> tuple | None:
    res = None
    min_ = len(text)

    for i, letter in enumerate(text):
        diff = text.find(letter, i+1) - i
        if min_ > diff > 0:
            res = (diff, letter)
            min_ = diff

    return res
