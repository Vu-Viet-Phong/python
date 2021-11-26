import random

numbersOfStreaks = 0
for experimentNumber in range(1000):
    # Code that creates a list of 100 'heads' or 'tails' value.
    lst = []
    for i in range(100):
        if random.randint(0, 1) == 0:
            lst.append('H')
        else:
            lst.append('T')

    # Code that checks if there is a streak of 6 heads or tails in a row.
    count = 1
    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1]:
            count += 1
            if count == 6:
                numbersOfStreaks += 1
                s = 1
        else:
            s = 1

print('Chance of streak: %s%%' % (numbersOfStreaks / 100))