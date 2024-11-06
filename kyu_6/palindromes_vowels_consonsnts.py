# Given a string, we'd like to know whether the vowels,
# consonants or both (assessed separately) are the same
# backwards as they are forwards. See examples at the
# bottom of this description.
#
# The test should be case-insensitive, and should only
# assess letters, ignoring spaces, numbers and other
# non-letter characters ("_" "*" " " "-"). Vowels are AEIOU.
# The letter Y is a consonant for this exercise.
#
# If the string doesn't have the same sequence of consonants
# or vowels backwards, we want to return "neither". If only
# the vowels are palindromic, return "vowel". If only the
# consonants are palindromic, return "consonant". If the
# vowels and the consonants in the string are palindromic,
# return "both".
#
# You can assume that all test cases will contain at least
# one vowel and one consonant.


import re


def palindrome(s: str) -> str:
    s = ''.join(re.findall('\\w', s))
    vowels = ''.join(re.findall('[aeiou]', s, re.I))
    consonants = ''.join(re.findall('[^aeiou_0-9]', s, re.I))
    if vowels.lower() == vowels[::-1].lower() and consonants.lower() == consonants[::-1].lower():
        return 'both'
    if vowels.lower() == vowels[::-1].lower():
        return 'vowel'
    if consonants.lower() == consonants[::-1].lower():
        return 'consonant'
    return 'neither'
