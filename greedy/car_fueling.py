
def compute_min_refills(distance, tank, stops):
    num_of_refills = 0
    current_stop = 0
    while current_stop + tank <= distance:
        current_stop = step(current_stop, tank, stops, index_of_current_stop(current_stop, stops))
        num_of_refills += 1
    return num_of_refills


def step(current_stop, tank, stops, i):
    while i < len(stops) and current_stop + tank >= stops[i]:
        i += 1
    return stops[i - 1]


def index_of_current_stop(current_stop, stops):
    try:
        index = stops.index(current_stop)
        return index
    except:
        return 0

    # print(step(1000, 400, [1000, 1100, 1200, 1300, 1450]))


# 2100 400 14 150 350 600 700 800 1000 1100 1200 1300 1450 1500 1600 1700 1800


if __name__ == '__main__':
    d, m, _, *stops = map(int, input().split())
    print(compute_min_refills(d, m, stops))
