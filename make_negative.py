#return an negetive 
#example  make_negative(1);  # return -1
#         make_negative(-5); # return -5
#         make_negative(0);  # return 0

def make_negative( number ):
    return -abs(number)

def make_negative( number ):
    return number if number < 0 else -number