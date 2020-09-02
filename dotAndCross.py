# You are given two arrays a and b. Both have dimensions of n X n.
# Your task is to compute their matrix product.

# Input Format

# The first line contains the integer n .
# The next n lines contains n space separated integers of array a.
# The following n  lines contains n space separated integers of array b .

# Output Format

# Print the matrix multiplication of a and b.

import numpy


a = int(input())
arr1 = numpy.array([list(map(int,input().split())) for _ in range(a)])
arr2 = numpy.array([list(map(int,input().split())) for _ in range(a)])
print(numpy.dot(arr1,arr2))
