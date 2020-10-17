import math
time = float(input("Digite o tempo em segundos: ")) #digit the time in seconds 

#the calculus:
min = time // 60
h = min // 60
sec = time % 60

#anwser
print(time, "segundos equivalem a:") #these 'x' seconds equals to:
print(h," horas,", min, " minutos e", sec,"segundos") #'x' hours, 'y' minutes and 'z' seconds