def unique_in_order(sequence):
    if not sequence:
        return []
    new_seq = [sequence[0],]
    for item in sequence:
        if item != new_seq[-1]:
            new_seq.append(item)

    return new_seq


print(unique_in_order('AAAABBBCCDAABBB'))
