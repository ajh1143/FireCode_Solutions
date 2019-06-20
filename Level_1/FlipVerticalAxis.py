"""
You are given an m x n 2D image matrix (List of Lists) where each integer represents a pixel. 

Flip it in-place along its vertical axis.

Example:
Input image :
1 0              
1 0 

Modified to :
0 1              
0 1
"""
```Python3
def flip_vertical_axis(matrix):
    for _ in matrix:
        _.reverse()
    return matrix
```
