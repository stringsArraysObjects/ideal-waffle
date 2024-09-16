#PARAMS: There will always be only one integer that appears an odd number of times.
#RESULTS: Given an array of integers, find the one that appears an odd number of times.
#EXAMPLE: [0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).

def find_it(seq):
    return [x for x in seq if seq.count(x) % 2][0]