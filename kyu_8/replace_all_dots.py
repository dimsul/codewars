# The code provided is supposed replace all the dots . in
# the specified String str with dashes -
#
# But it's not working properly.
#
# def replace_dots(s):
#     return re.sub(r'.', '-', s)
#
# Task
# Fix the bug, so we can all go home early.
#
# Notes
# String str will never be null.


import re


def replace_dots(s: str) -> str:
    return re.sub('\\.', '-', s)
