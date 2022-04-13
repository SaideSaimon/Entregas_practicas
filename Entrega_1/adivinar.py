
# Adivina adivinador....
import random

numero_aleatorio = random.randrange(101)
gane = False
print("Tenés 3 intentos para adivinar un entre 0 y 99")
intento = 1
max_intentos = 5
while intento <= max_intentos and not gane:
    numero_ingresado = int(input('Ingresa tu número: '))
    if numero_ingresado == numero_aleatorio:
        print(f"Ganaste! y necesitaste {intento} intentos!!!")
        gane = True
    else:
        print('Mmmm ... No.. ese número no es... Seguí intentando.')
    intento += 1
if not gane:
    print(f"\n Perdiste :(\n El número era: {numero_aleatorio}")
