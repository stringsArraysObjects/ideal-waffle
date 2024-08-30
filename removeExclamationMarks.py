# PARAMS: 
#RESULT: remove all exclamation marks from the end of a sentence.
#EXAMPLE: "Hi!"     ---> "Hi"
#         "Hi!!!"   ---> "Hi"
#PSEUDOCODE: use the rstrip() method to remove chars
#            from the end of a string.

def remove(st):
    return st.rstrip('!')