def compare_ends(words):
    itog = 0
    for i in words:
        sum = len(i)
        if sum > 2 and i[-1:] == i[:1]:
            itog = itog + 1
    return itog
