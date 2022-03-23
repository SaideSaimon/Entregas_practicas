
# Adivina adivinador....
import random

numero_aleatorio = random.randrange(101)
gane = False
print("Tenés 3 intentos para adivinar un entre 0 y 99")
intento = 1
max_intentos = 5
# Iteración de intentos
while intento <= max_intentos and not gane:
	numero_ingresado = int(input('Ingresa tu número: '))
	if numero_ingresado == numero_aleatorio:
		print('Ganaste! y necesitaste {} intentos!!!'.format(intento))
		gane = True
	else:
		print('Mmmm ... No.. ese número no es... Seguí intentando.')
	intento += 1
if not gane:
	print('\n Perdiste :(\n El número era: {}'.format(numero_aleatorio))
