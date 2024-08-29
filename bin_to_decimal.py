#PARAMS: binary num given as a string.
#RESULT: convert a binary num to a decimal num.
#EXAMPLE: 
#PSEUDOCODE: convert binary string to decimal by specifying base
#            2 as a parameter of the int() function.

def bin_to_decimal(inp):
    return int(inp, 2)