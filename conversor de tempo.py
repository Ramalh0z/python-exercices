import math
t = input(" ")
min = t // 60
s = t % 60
h = min // 60
print(h, ':', min,':', s)