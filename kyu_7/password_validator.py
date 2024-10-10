# Your job is to create a simple password validation function,
# as seen on many websites.
#
# The rules for a valid password are as follows:
#
# There needs to be at least 1 uppercase letter.
# There needs to be at least 1 lowercase letter.
# There needs to be at least 1 number.
# The password needs to be at least 8 characters long.
# You are permitted to use any methods to validate the password.
#
# Extra info
# - You will only be passed strings.
# - The string can contain any standard keyboard character.
# - Accepted strings can be any length, as long as they are 8 characters or more.


import re


def password(st):
    if (len(st) > 7 and
            re.search('[0-9]', st) and
            re.search('[a-z]', st) and
            re.search('[A-Z]', st)):
        return True

    return False
