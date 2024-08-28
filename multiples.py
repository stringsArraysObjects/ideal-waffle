# Basically fizzbuzz but with different words and a 
# default word "Miss"

def multiple(x):
    return 'Bang' * (x % 3 == 0) + 'Boom' * (x % 5 == 0) or 'Miss'

def multiple(x):
    if x % 3 == 0 and x % 5 == 0:return "BangBoom"
    if x % 3 == 0: return "Bang"
    if x % 5 == 0:return "Boom"
    else:return "Miss"

print ("\n".join(multiple(x) for x in range(1, 21)))