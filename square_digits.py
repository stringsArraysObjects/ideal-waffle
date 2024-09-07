#RESULT:    square every digit of a number and concatenate them
#EXAMPLE:   An input of 765 will/should return 493625 because 72 is
#           49, 62 is 36, and 52 is 25. (49-36-25)
#PSEUDOCODE:  This uses the join() method to concatenate 
#             each character of the string with a space in between.
#             Iterates over each character in the string num.
#             convert variable back to an int.
#             do the math.
#             concatenate
#             convert result to int 
#        


def square_digits(num):
    return int(''.join(str(int(d)**2) for d in str(num)))