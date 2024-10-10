# Write an algorithm that will identify valid IPv4 addresses
# in dot-decimal format. IPs should be considered valid if
# they consist of four octets, with values between 0 and 255, inclusive.
#
# Notes:
# - Leading zeros(e.g. 01.02.03.04) are considered invalid
# - Inputs are guaranteed to be a single string


import re


def is_valid_ip(strng: str) -> bool:
    if re.search('((\\.|^)0\\d+|\\n)', strng) or not re.search('^(\\d+[.]){3}\\d+$', strng):
        return False
    for num in map(int, strng.split('.')):
        if num > 255:
            return False
    return True
