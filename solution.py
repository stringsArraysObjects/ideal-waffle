#PARAMS:  If the number is a multiple of both 3 and 5, only count it once.
#RESULT:  returns the sum of all the multiples of 3 or 5 below the number passed in.
#EXAMPLE: 
#PSEUDOCODE:  use the range() function to loop through a sequence
#             of numbers using the variable number as the range,
#             then use the sum function to add the identified numbers.
def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)