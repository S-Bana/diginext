def swap(arr, a, b):
    """ swap elements a and b in an array """
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp


def selection_sort(unsorted):
    """ selection sort algorithm """
    # Input length
    in_length = len(unsorted)
    # iterate over array
    for i in range(0, in_length):
        # initialise with first value
        current_min = unsorted[i]

        # min_index initializer
        min_index = i

        # iterate over remaining unsorted items
        for j in range(i, in_length):
            # check if jth value is less than current min
            if unsorted[j] < current_min:
                # update minimum value and index
                current_min = unsorted[j]
                min_index = j

        # check if ith and min_index values are not equal
        if i != min_index:
            # swap ith and jth values
            swap(unsorted, i, min_index)
            # Print swap values and array
            print(i, min_index, data)


# ===================================================================
""" Run code """

data = [7, 1, 3, 2, 4, 5, 6]

print("Unsorted Array")
print(data)
print(30*"-")

selection_sort(data)

print(30*"-")
print('Sorted Array')
print(data)
