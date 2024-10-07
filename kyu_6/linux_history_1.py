# In this kata you should complete a function that
# take in argument a history with the following format:
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
# and that should return the last executed command line,
# in this case it will be history.


import re


def bang_bang(history):
    return re.compile('\\s{2}[a-zA-Z].*$').findall(history)[-1].strip()
