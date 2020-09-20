medida = float(input("Digite a medida em metros:"))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000

print("A medida pode ser convertida em: ")
print(
"quilometros: {}km \n"
"hectometros: {}hm \n"
"decametros: {}dam \n"
"decimetros: {}dm \n"
"centimetros: {}cm \n"
"milimetros: {}mm \n".format
(km, hm, dam,dm, cm, mm)
)