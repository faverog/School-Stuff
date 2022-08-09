from sympy import init_printing, pprint
from sympy import Matrix, eye, zeros

init_printing()

# Import needed variables here
from sympy.abc import K, s, k, x, y, J, D, b, l, L, R

# Define matricies (Exponents are denoted by '**')
A = Matrix([[-2, 2, 1], [2, -2, 0], [-1, 0, 0]])
B = Matrix([[1], [-1], [1]])
C = Matrix([[1, -1, 0]])
D = Matrix([0])

#Define sI-A matrix
sI = s*eye(A.rows)
sI_minus_A = sI - A
pprint(sI_minus_A)

# Compute adjugate matrix
adj_sI_minus_A = sI_minus_A.adjugate()
pprint(adj_sI_minus_A)

# Compute determinant of the matrix
det_sI_minus_A = sI_minus_A.det()
pprint(det_sI_minus_A)

# Compute inverse matrix
inv_sI_minus_A = sI_minus_A.inv()
pprint(inv_sI_minus_A)

#Compute Transfer Function Model (Gs)
#this method of calculating allows sympy to simplify the numerator of the TF
Gs = D + (C*adj_sI_minus_A*B)/det_sI_minus_A
pprint(Gs)