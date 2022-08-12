from sympy import init_printing, pprint
from sympy import Matrix, eye, zeros

init_printing()

# Import needed variables here
from sympy.abc import K, s, k, x, y, J, D, b, l, L, R

# Define matricies (Exponents are denoted by '**')
# Example 3x3: Matrix([[-10, 0, -2], [0, 0, 1], [0.2, 0, -1]])
# Example 3x1: Matrix([[1], [1], [-1]])
# Example 1x3: Matrix([[0, 1, -1]])
A = Matrix([[0, 1, 0], [-1, -2, 2], [0, 2, -2]])
B = Matrix([[1], [1], [-1]])
C = Matrix([[0, 1, -1]])
D = Matrix([0])

#Define sI-A matrix
sI = s*eye(A.rows)
sI_minus_A = sI - A
print("\nsI-A Matrix")
pprint(sI_minus_A)

# Compute adjugate matrix
adj_sI_minus_A = sI_minus_A.adjugate()
print("\nAdjugate sI-A Matrix")
pprint(adj_sI_minus_A)

# Compute determinant of the matrix
det_sI_minus_A = sI_minus_A.det()
print("\nDeterminant of sI-A")
pprint(det_sI_minus_A)

# Compute inverse matrix
inv_sI_minus_A = sI_minus_A.inv()
print("\nInverse sI-A Matrix")
pprint(inv_sI_minus_A)

#Compute Transfer Function Model (Gs)
#this method of calculating allows sympy to simplify the numerator of the TF
Gs = D + (C*adj_sI_minus_A*B)/det_sI_minus_A
print("\nTransfer Function Model")
pprint(Gs)