# Selection Sort
lst = [8, 4, 2, 5, 2]

def selection_sort(lst_to_sort):
    length = len(lst_to_sort)
    for i in range(length):
        minimum = i

        for j in range(i+1, length):
            if lst_to_sort[j] < lst_to_sort[i]:
                minimum = j

        lst_to_sort[i], lst_to_sort[minimum] = lst_to_sort[minimum], lst_to_sort[i]


    return lst_to_sort


print(selection_sort(lst))