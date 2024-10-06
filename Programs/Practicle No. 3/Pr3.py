# Q : Write a Python Program to compute following computation on matrices :
#       a)  Addition of two matrices
#       b)  Subtraction of two matrices
#       c)  Multiplication of two matrices
#       d)  Transpose of a matix

import numpy as np

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

print("\nEnter the elements for the first matrix:")
matrix1 = []
for i in range(rows):
    row = list(map(int, input(f"\tEnter row {i+1} (space-separated) : ").split()))
    matrix1.append(row)

print("\nEnter the elements for the second matrix:")
matrix2 = []
for i in range(rows):
    row = list(map(int, input(f"\tEnter row {i+1} (space-separated) : ").split()))
    matrix2.append(row)

matrix1 = np.array(matrix1)
matrix2 = np.array(matrix2)

print("\nAddition of two matrices:")
add_result = matrix1 + matrix2
print(add_result)

print("\nSubtraction of two matrices:")
sub_result = matrix1 - matrix2
print(sub_result)

print("\nElement-wise Multiplication of two matrices:")
mult_result = matrix1 * matrix2
print(mult_result)

print("\nTranspose of the first matrix:")
transpose_result = np.transpose(matrix1)
print(transpose_result)