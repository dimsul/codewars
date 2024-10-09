# In this kata you should complete a function that take in
# a string that correspond to s, and a history with the following format:
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
# and that should return the most recent command line that start with s,
# for example with s="more" and the above history it should return more me.
# If user ask for an s without any know entry for example n=mkdir here,
# the function should return !mkdir: event not found.


import re


def bang_start_string(n, history):
    res = re.findall(f'\\s\\s{n}.*\\n', history+'\n')
    res = res[-1] if res else f'!{n}: event not found'
    return res.strip('\n ')
