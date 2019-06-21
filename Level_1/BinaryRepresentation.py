"""
Write a function to compute the binary representation of a positive decimal integer. 

The method should return a string. 

Example:
dec_to_bin(6) ==> "110"
dec_to_bin(5) ==> "101"

Note : Do NOT use in-built bin() function.
"""
def dec_to_bin(number):
    if number < 2:
        return str(number)
    else:
        return dec_to_bin(number/2) + dec_to_bin(number%2)
