"""
Task

You are given two integer arrays of size N X P and M X P (N & M are rows, and P is the column). 
Your task is to concatenate the arrays along axis 0 .
"""


import numpy


n, m, p = map(int, input().split())
array = numpy.array([input().split() for i in range(n+m)], int)

print(array)
