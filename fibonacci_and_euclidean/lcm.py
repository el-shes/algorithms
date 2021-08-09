# Uses python3

def lcm_naive(a, b):
    if a > b:
        greater = a
    else:
        greater = b

    while True:
        if ((greater % a == 0) and (greater % b == 0)):
            lcm = greater
            break
        greater += 1

    return lcm

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm_naive(a, b))

