# In this kata you should complete a function that
# take in an integer that correspond to n, and a
# history with the following format:
#
#   1  cd /pub
#   2  more beer
#   3  lost
#   4  ls
#   5  touch me
#   6  chmod 000 me
#   7  more me
#   8  history
#
# and that should return the nth executed command line,
# for example with n=4 and the above history it should
# return ls. If user ask for a without any know entry
# for example n=12 here, the function should return !12:
# event not found. Note: For this kata we will assume that n >= 1.


import re


def bang_n(n, history):
    res = re.search(f'{n}.*(\\n|$)', history)
    return re.search("[a-zA-Z].*[a-zA-Z0-9.]", res.group(0)).group(0) if res else f"!{n}: event not found"
