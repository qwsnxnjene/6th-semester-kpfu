# import sys
import time


def gcd(a, b):
    start = time.time()

    time.sleep(1)

    a, b = max(a, b), min(a, b)
    k = 0
    if b == 0:
        return b, k, (time.time() - start) - 1

    k += 1
    c = a % b
    while c != 0:
        a, b = b, c
        c = a % b
        k += 1
    return b, k, (time.time() - start) - 1


# sys.set_int_max_str_digits(5000)
# A, B = int('9' * 5000), int('8' * 5000)
# print(A)
# print(B)
# print(gcd(A, B))
print(gcd(210, 45))
print(gcd(77, 7))
print(gcd(100, 0))
print(gcd(100, 1))
