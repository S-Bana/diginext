def fun_task_two(s=""):
    # counter
    tally_ = 0

    # min_index initializer
    min_index = s[0]

    # output value
    out_value = min_index

    # iterate over string
    for i in s[1:]:
        # check if ith and min_index values are equal
        if i == min_index:
            # counter is work
            tally_ += 1
        # check if ith and min_index values are not equal
        else:
            # update min_index value and out_value
            min_index = i
            out_value += i

    return out_value, tally_


# ===================================================================
""" Run code """

data = "abbbaba"

print(f"unordered string: {data}")
print(30*"-")

data, tally = fun_task_two(data)

print(f'Ordered string: {data}')
print(30*"-")

print(f'Minimum characters that need to be removed: {tally}')
