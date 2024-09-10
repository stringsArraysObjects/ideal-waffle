# RESULT: return the sum of all the positive numbers in
#         the array.
#EXAMPLE: [1,-4,7,12] => 1 + 7 + 12 = 20
#PSEUDOCODE: use for loop to iterate over the array
#            testing each element with a comparison
#            expression. Sum all elements that pass
#            the test.

def positive_sum(arr):
    return sum(n for n in arr if n>0)