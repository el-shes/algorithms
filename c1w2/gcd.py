# Uses python3
import time

def gcd_naive(a, b):
    if a > b:
        bigger = a
        smaller = b
    else:
        bigger = b
        smaller = a
    while smaller != 0:
        remainder = bigger % smaller
        bigger = smaller
        smaller = int(remainder)
    return bigger


if __name__ == "__main__":
    a, b = map(int, input().split())
    start_time = time.time()
    print(gcd_naive(a, b))
    gcd_estimated_time = (time.time() - start_time)
    print(gcd_estimated_time)
