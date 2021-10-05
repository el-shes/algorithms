def bubble_sort(lst):
    for num in range(len(lst)-1, 0, -1):
        for i in range(num):
            if lst[i] > lst[i+1]:
                lst[i], lst[i + 1] = lst[i+1], lst[i]
    return lst

to_sort = [54,15,93,17,71,31,55,55,20]


if __name__ == '__main__':
    print(bubble_sort(to_sort))