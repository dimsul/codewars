import time


def closure_gen(*s):

    try:

        given_set = set(s)
        new_set = set()
        new_set.add(min(given_set))

        while True:

            yield max(new_set)

            diff = {i*j for j in new_set for i in given_set}.union(given_set).difference(new_set)

            new_set.add(min(diff))

    except Exception:

        return


for val in closure_gen(1):
    print(val, end=' ')
    time.sleep(1)
