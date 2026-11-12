import sympy as sp

x,y = sp.symbols("x, y")
M = sp.eye(6)
(M[0,0], M[0,1], M[0,2], M[0,3], M[0,4], M[0,5]) = (x**2, x*y, y**2,x,y,1)
for i in range(1,6):
    x_1 = float(input("Point " + str(i)+ " x-cordinate: "))
    y_1 = float(input("Point " + str(i)+ " y-cordinate: "))
    (M[i,0], M[i,1], M[i,2], M[i,3], M[i,4], M[i,5]) = (x_1**2, x_1*y_1, y_1**2,x_1,y_1,1)

print(M)
print()
print(str(M.det()) + " = 0")