# Task
#
# Write a function that receives a non-negative integer n ( n >= 0 )
# and returns the next higher multiple of five of that number,
# obtained by concatenating the shortest possible binary string
# to the end of this number's binary representation.


def next_multiple_of_five(n: int) -> int:

    n = 4 if n == 0 else n

    category = 0
    run = True
    while run:
        category += 1
        num = 0
        while len(format(num, 'b')) <= category:
            if int(format(n, 'b') + format(num, 'b').zfill(category), 2) % 5 != 0:
                num += 1
            else:
                run = False
                break

    return int(format(n, 'b') + format(num, 'b').zfill(category), 2)


def next_multiple_of_five_2(n: int, category=1) -> int:
    n = 1 if n == 0 else n
    num = 0
    while len(format(num, 'b')) <= category:
        if int(format(n, 'b') + format(num, 'b').zfill(category), 2) % 5 != 0:
            num += 1
        else:
            return int(format(n, 'b') + format(num, 'b').zfill(category), 2)

    return next_multiple_of_five_2(n, category + 1)
