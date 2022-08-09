from sympy import init_printing
from sympy import Matrix

init_printing()

# Import needed variables here
from sympy.abc import K, s, k, x, y, J, D, b, l, L, R

# Define matrix (Exponents are denoted by '**')
A = Matrix([[s, s+1], [2*s+1, s/s+3]])

# Compute adjugate matrix
adj_A = A.adjugate()
print(adj_A)

# Compute determinant of the matrix
det_A = A.det()
print(det_A)

# Compute inverse matrix
inv_A = A.inv()
print(inv_A)







