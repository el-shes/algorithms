# Merge Sort
lst = [7, 5, 2, 3, 7, 13, 1, 6, 3, 1, 2]


def merge_sort(lst_to_sort):
    if len(lst_to_sort) > 1:
        middle = len(lst_to_sort) // 2
        first = lst_to_sort[:middle]
        second = lst_to_sort[middle:]

        left = merge_sort(first)
        right = merge_sort(second)

        result = merge(left, right)
        return result

    else:
        return lst_to_sort


def merge(left, right):
    sorted_lst = []
    left_counter = 0
    right_counter = 0
    while left_counter < len(left) and right_counter < len(right):
        if left[left_counter] <= right[right_counter]:
            sorted_lst.append(left[left_counter])
            left_counter += 1
        elif left[left_counter] > right[right_counter]:
            sorted_lst.append(right[right_counter])
            right_counter += 1

    for el in right[right_counter:]:
        sorted_lst.append(el)
    for el in left[left_counter:]:
        sorted_lst.append(el)

    return sorted_lst

print(merge_sort(lst))
