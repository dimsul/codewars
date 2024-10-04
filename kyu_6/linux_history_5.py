# In this kata you should complete a function that take in
# an string that correspond to s, and an history with the following format:
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
# and that should return the most recent command line that contains
# executed command line s, for example with s="me" and the above
# history it should return more me. If user ask for a s without any
# know entry for example n=you here, the function should return
# !you: event not found.


import re


def bang_contain_string(s, history):
    s_replace = s.replace('.', '\\.').replace('|', '\\|')
    result = re.compile(f'\\d\\s\\s.*{s_replace}.*\n').findall(history+'\n')
    if result:
        return result[-1].strip('\n').split('  ')[-1]
    else:
        return f'!{s}: event not found'
