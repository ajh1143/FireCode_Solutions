"""
Given an list containing 9 numbers ranging from 1 to 10, write a function to find the missing number. 
Assume you have 9 numbers between 1 to 10 and only one number is missing.

Example:
input_list: [1, 2, 4, 5, 6, 7, 8, 9, 10]
find_missing_number(input_list) => 3
"""

def find_missing_number(list_numbers):
    ranger = list(range(1,11))
    solution = [int(x) for x in ranger if x not in list_numbers]
    return solution[0]

