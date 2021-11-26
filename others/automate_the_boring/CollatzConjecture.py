"""Collatz Conjecture."""
def collatz(n):
    while n > 1:
        print(n)
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = int(3 * n + 1)
    else:
        print(n)

n = int(input('Enter the first term of the sequence: '))
collatz(n)