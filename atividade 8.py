import math
r = float(input("Raio da circunferencia: "))
a = float(input("Medida do Ângulo em graus: "))

if (1.0 > r < 50.0) and (0.0 > a < 359.0):
	t = 3.14 * (r * r)
	c = a * 3.14 * r / 180

#v1 = round(set, 2)
#v2 = round(arc, 2)
#print(v1, v2)
print( t, c)