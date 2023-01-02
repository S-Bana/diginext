def fun_task_one(i=1, s=""):
    # Create text with input data
    temp = s * i
    # Select the text
    temp = temp[0:i]
    # Return Answers
    return temp.count('a'), temp


# ===================================================================
""" Run code """

data = "qa"
length = 10

print(f"Input: {data} , length: {length}")
print(30 * "-")

cunt, data = fun_task_one(length, data)

print(f"Output: {data} \nRepeat 'a': {cunt}")
