"""
Task
You are given a 1-D array,A . Your task is to print the floor, ceil and rint of all the elements of A.

Input Format

A single line of input containing the space separated elements of array A.

Output Format

On the first line, print the floor  of A.
On the second line, print the ceil of A.
On the third line, print the rint  of A.


"""


import numpy


numpy.set_printoptions(legacy='1.13')
new_array = numpy.array(input().split(),float)
print(numpy.floor(new_array))
print(numpy.ceil(new_array))
print(numpy.rint(new_array))
