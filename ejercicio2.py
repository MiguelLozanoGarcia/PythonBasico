#La nota del trimestre está basada en
#Nota hito individual = 30 %
#Nota hito grupal = 20 %
#Nota examen = 50 %


individual=int(input('nota del hito individual'))
grupal=int(input('nota del hito grupal'))
examen=int(input('nota del examen'))

i=individual*30/100
g=grupal*20/100
e=examen*20/100

notaTrimestre=i+g+e
print(f' tu nota es {notaTrimestre}')

