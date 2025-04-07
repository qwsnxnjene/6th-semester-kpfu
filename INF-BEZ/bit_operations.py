import random


def generate_long_num_1(k: int):
    if k == 1:
        start = 0
    else:
        start = 2**(k - 1)
    end = 2**k

    return random.randint(start, end - 1)


def generate_long_num_2(k: int):
    n = random.getrandbits(k)

    start = 2 ** (k - 1)
    end = 2 ** k - 1

    if start <= k <= end:
        return n

    return n + start


def generate_odd_long_number(k: int):
    randomN = generate_long_num_1(k)

    if randomN % 2 == 1:
        return randomN
    else:
        return randomN + 1


print(generate_long_num_1(4))
print(generate_long_num_2(4))
print(generate_odd_long_number(4))
