"""
Write a function - duplicate_items to find the redundant or repeated items in a list and return them in sorted order. 
This method should return a list of redundant integers in ascending sorted order (as illustrated below). 

Examples:
duplicate_items([1, 3, 4, 2, 1]) => [1]

duplicate_items([1, 3, 4, 2, 1, 2, 4]) => [1, 2, 4]
"""


def duplicate_items(list_numbers):
    holder = {}
    for each_element in list_numbers:
        element_count = list_numbers.count(each_element)
        if element_count > 1:
            holder[each_element] = element_count
    solution = list(holder.keys())
    return solution

