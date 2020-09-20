#limite das temperaturas 
vmc = -273.0
vmf = -459.67
vmk = 0.0

m = input(" ")
t = float(input(" "))

#Celsius
if (m == "C" or "c"):
	temp_f = (9 *  t / 5) + 32
	temp_k = t + 273.0
	
	if (temp_f >= vmf or temp_k >= vmk):
		print(temp_f, " F")
		print(temp_k, " K")
	else: print("Valor de temperatura abaixo do minimo")

#Fahrenheit
elif (m == "F" or "f"):
	temp_k = (t - 32) * 5/9 + 273.0
	temp_c = (t - 32) * 5/9
	
	if (temp_c >= vmc or temp_k >= vmk):
		print(temp_c, " C")
		print(temp_k, " K")
	else: print("Valor de temperatura abaixo do minimo")

#Kelvin	
elif (m == "K" or "k"):
	temp_f = (t - 273.15) * 9/5 + 32
	temp_c = t - 273.0
	
	if (temp_c >= vmc or temp_f >= vmf):
		print(temp_f, " F")
		print(temp_c, " C")
	else: print("Valor de temperatura abaixo do minimo")