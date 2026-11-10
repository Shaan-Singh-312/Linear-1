import sympy as sp
import numpy as np

sp.init_printing()
# SymPy: exact entries
A = sp.Matrix([[2, 1], [1, 2]])
v = sp.Matrix([1, 2, 3]) # column vector
# Use Rational for fractions; a bare 1/3 becomes a float
h = sp.Rational(1, 3) # exact 1/3
a, b = sp.symbols('a b')
S = sp.Matrix([[a, b], [b, a]]) # symbolic matrix; S.det() gives a**2 -
b**2

# NumPy: float entries
A_n = np.array([[2, 1], [1, 2]], dtype=float)
v_n = np.array([1, 2, 3])
# Convert between them
A_n = np.array(A, dtype=int) # SymPy -> NumPy
A = sp.Matrix(A_n) # NumPy -> SymPy (floats stay floats)
A[0,0] = 1

#print(S.det())
#print(A)
#print(sp.eye(5))


x, y, z = sp.symbols('x y z')
M = sp.Matrix([[1, 2, -1, 3], [2, 4, 1, 9], [1, 2, 2, 6]]) # augmented [A |b]
M.rref() # rows [1,2,0,4], [0,0,1,1], [0,0,0,0]; pivots (0,2)
#print(sp.linsolve(M, x, y, z)) # {(4 - 2*y, y, 1)}

#print(np.eye(5))
#print(sp.eye(3))

#print(np.random.default_rng().integers(-5, 5, (3,3)))
b = sp.Matrix([[1], [1], [1]])
M = sp.Matrix([[1,1, 1], [2,-1,1], [2,1,1]])
A = M
print(M)
print(A.rref())
A = M
print(A.echelon_form())
print(M.rank())
print(b)
print(sp.linsolve((M,b),x,y,z))
print(M.nullspace())
print("----------------")
print(M.LUdecomposition())