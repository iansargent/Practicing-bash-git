"""
Ian Sargent
CS 1210
10/5/20234
"""


def next_collatz(n):
    if n % 2 == 0:
        n = n / 2
    elif n % 2 == 1:
        n = (3 * n) + 1
    elif n / 2 == 1:
        print(1)
    return int(n)


if __name__ == '__main__':

    n = int(input('Enter an integer greater than 1: '))

    lst = [n]

    while n <= 1:
        print('Invalid Input')
        n = int(input('Enter an integer greater than 1: '))

    while n > 1:
        if n % 2 == 0:
            n = n / 2
            lst.append(int(n))
        elif n % 2 == 1:
            n = (3 * n) + 1
            lst.append(int(n))
        elif n / 2 == 1:
            lst.append(int(n))

    print(lst)

    print(f'The length of the sequence is {len(lst)}.')
