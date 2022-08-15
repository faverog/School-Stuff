from sympy import init_printing, pprint
from sympy import Matrix, eye, zeros

init_printing()

# Import needed variables here
from sympy.abc import K, s, k, x, y, J, D, b, l, L, R

# Enter TF
# Assuming that no orders of s are skipped in denominator
numerator = [2, 1, 1]
denominator = [1, 4, 1, 2]
denominator.reverse()

# Create A matrix
rows_in_A = len(denominator) - 1
A = []
for i in range(rows_in_A-1):
    row = []
    for j in range(rows_in_A):
        if j == i + 1:
            row.append(1)
        else:
            row.append(0)
    A.append(row)

last_row = [-1*denominator[i] for i in range(rows_in_A)]
A.append(last_row)

# Create B vector 
B = []
for i in range(rows_in_A-1):
    B.append([0])
B.append([1])

# Create C vector
zero_padding = [0] * (len(denominator) - len(numerator) - 1)
C = numerator
C.reverse()
C += zero_padding
C = [C]

# Output results
print("\nA Matrix:")
pprint(Matrix(A))

print("\nB Vector:")
pprint(Matrix(B))

print("\nC Vector:")
pprint(Matrix(C))




