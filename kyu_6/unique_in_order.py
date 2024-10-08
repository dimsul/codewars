# Implement the function unique_in_order which takes as argument a
# sequence and returns a list of items without any elements with
# the same value next to each other and preserving the original
# order of elements.
from typing import Union


def unique_in_order(sequence: Union[str, list, tuple]) -> list:
    if not sequence:
        return []
    new_seq = [sequence[0],]
    for item in sequence:
        if item != new_seq[-1]:
            new_seq.append(item)

    return new_seq
