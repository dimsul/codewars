# Task
# There's a vote made for 30 candidates numbered from 1 to 30. Each person votes for each of the 30
# candidates and this voting is saved in an integer (you're trying to use the least space possible).
#
# Candidate 1 is on the first bit of the integer, candidate 2 in the second bit and so on.
#
# If the bit is set, the candidate received a vote. There are up to 1000 voters that all voted.
#
# In this elections there can only be a unanimous winner. Output the number of the winner or 0 if
# there are no winners or multiple winners.
#
# The votes made by the voters are given in an array of integers.
#
# In this case the input array would be: [704643076, 939524208, 603979956] and the output would be: 30
# because candidate 30 was the only one who received votes from each voter.


# Solution
def judge(votes):
    res = []
    win_points = len(votes)
    for i in range(0, 30):
        print(i)

        try:
            for vote in votes:
                if vote % 2 == 0:
                    raise Exception
            res.append(i)
        except Exception:
            pass

        votes = [vote >> 1 for vote in votes if vote >> 1 > 0]
        if len(votes) < win_points:
            break

    if 0 < len(res) < 2:
        return res[0] + 1

    return 0
