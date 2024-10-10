# Complete the solution so that it splits the string into
# pairs of two characters. If the string contains an odd
# number of characters then it should replace the missing
# second character of the final pair with an underscore ('_').


import re


def solution(s):
    s = s if len(s) % 2 == 0 else f'{s}_'
    return re.findall('\\w{2}', s)


print(solution("asdfads"))
