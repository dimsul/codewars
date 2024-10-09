# In this kata you should complete a function that take in
# an integer that correspond to n, and a history with the following format:
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
# for example with n=4 and the above history it should return touch me.
# If user ask for an n without any know entry for exampl n=12 here,
# the function should return !12: event not found.


import re


def bang_minus_n(n, history):
    res = tuple(map(int, re.findall('\\s{2}\\d+\\s{2}', history)))
    if not res or res[-1] - n + 1 not in res:
        return f'!-{n}: event not found'
    res = re.search(f'{res[-1] - n + 1}'+'\\s{2}.*(\\n|$)', history).group(0)
    return re.search('[a-zA-Z].*[^\\n$\\s]', res).group(0)


def bang_minus_n2(n, history):
    res = {re.search('^\\d+', sub_str).group(0): re.search('[a-zA-Z].*[^\\n$\\s]', sub_str).group(0)
           for sub_str in re.findall('\\d+\\s{2}.*\\n', history+'\n')}

    return res[str(len(res) - n + 1)] if str(len(res) - n + 1) in res else f'!-{n}: event not found'
