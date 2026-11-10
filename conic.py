import sympy as sp

points = []
for i in range(5):
    points.append(float(input("Point " + str(i+1)+ " x-cordinate: ")))
    points.append(float(input("Point " + str(i+1)+ " y-cordinate: ")))
x,y = sp.symbols("x, y")
M = sp.Matrix([[x**2, x*y, y**2, x, y, 1], [points[0]**2, points[0]*points[1], points[1]**2, points[0], points[1], 1], [points[2]**2, points[2]*points[3], points[3]**2, points[2], points[3], 1], [points[4]**2, points[4]*points[5], points[5]**2, points[4], points[5], 1],[points[6]**2, points[6]*points[7], points[7]**2, points[6], points[7], 1], [points[8]**2, points[8]*points[9], points[9]**2, points[8], points[9], 1]])
print(M)
print()
print(M.det() * (25/192))