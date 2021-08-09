# Uses python3
import time

def calc_fib(n):
    fib_numbs = [0,1,1]
    if (n <= 1):
        return n
    for i in range(3, n+1):
        fib_numbs.append(fib_numbs[-1] + fib_numbs[-2])
    return fib_numbs[-1]

def calc_fib_rec(n, first, second):
    if(n==0):
        return first+second
    else:
        return calc_fib_rec(n-1, second, first+second)


n = int(input())
start_time1 = time.time()
print(calc_fib(n))
fib_count_estimated_time = (time.time() - start_time1)
print(fib_count_estimated_time)

start_time2 = time.time()
print(calc_fib_rec(n-2, 0, 1))
fib_rec_time = (time.time() - start_time2)
print(fib_rec_time)
