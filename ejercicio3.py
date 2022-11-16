#Se pide calcular la nota de tu examen tipo test.
#Serán 20 preguntas
#Las preguntas correctas sumarán 0,5
#Las preguntas incorrectas restarán 0,25
#Las preguntas sin contestar tendrán 0

numerocorrectas=int(input('¿cuantas preguntas han sido correctas?'))
numeroincorrectas=int(input('¿cuantas preguntas han sido incorrectas?'))
nota=numerocorrectas*0.5-numeroincorrectas*0.25
print(f'tu nota es {nota}')

