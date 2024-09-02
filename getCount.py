#PARAMS: y is not a vowel in this exercise
#         The input string will only consist of 
#         lower case letters and/or spaces.
#RESULT:  Return the number (count) of vowels in the given string.
#EXAMPLE: 
#PSEUDOCODE:  use the sum() function as a counter to tally
#             the occurances of vowels in the given string.

def get_count(sentence):
    return sum(1 for let in sentence if let in "aeiouAEIOU")