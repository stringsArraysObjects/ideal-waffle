# PARAMS: There will always be at least one number in the input string.
# RESULT: Return the highest and lowest number.
# EXAMPLE: high_and_low("1 2 3 4 5")  # return "5 1"
# PSEUDOCODE: Split chars, treat as numbers, iterate
#             over the string sort out max and min.

def high_and_low(numbers):
    return " ".join(x(numbers.split(), key=int) for x in (max, min))