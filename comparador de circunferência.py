r1 = float(input("Valor do Primeiro Raio:"))
r2 = float(input("Valor do Segundo Raio:"))
circun1 = 2 * 3.14 * r1
circun2 = 2 * 3.14 * r2

if (circun1 > circun2):
	print("O Primeiro Circulo é maior")
if (circun2 > circun1):
	print("O Segundo Circulo é maior")
if (circun1 == circun2) or (circun2 == circun1):
	print("São iguais")