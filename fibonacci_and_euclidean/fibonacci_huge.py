# Uses python3
import time


def pisanoPeriod(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current = current, (previous + current) % m
        # A Pisano Period starts with 01
        if (previous == 0 and current == 1):
            return i + 1


def get_fibonacci_huge_naive(n, m):
    p = pisanoPeriod(m)
    n = n % p
    if (n <= 1):
        return n
    else:
        previous, current = 0, 1
        for i in range(2, n + 1):
            previous, current = current, (previous + current)
    return current % m


if __name__ == '__main__':
    n, m = map(int, input().split())
    start_time = time.time()
    print(get_fibonacci_huge_naive(n, m))
    huge_fib_mod_estimated_time = (time.time() - start_time)
    print(huge_fib_mod_estimated_time)


#2816213588 239
#239 1000