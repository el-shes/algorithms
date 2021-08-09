# Uses python3
import time
from fibonacci_and_euclidean import fibonacci


def get_fibonacci_last_digit_naive(n):
    return fibonacci.calc_fib(n) % 10



def get_fibonacci_last_digit_cool(n):
    fib_numbs = [0, 1, 1]
    if (n <= 1):
        return n
    for i in range(3, n + 1):
        fib_numbs.append((fib_numbs[-1] + fib_numbs[-2]) % 10)
    return fib_numbs[-1]


if __name__ == '__main__':
    n = int(input())
    start_time = time.time()
    print(get_fibonacci_last_digit_naive(n))
    last_dig_estimated_time = (time.time() - start_time)
    print(last_dig_estimated_time)

    start_time1 = time.time()
    print(get_fibonacci_last_digit_cool(n))
    cool_estimated_time = (time.time() - start_time1)
    print(cool_estimated_time)

