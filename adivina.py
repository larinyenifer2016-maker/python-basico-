import random

def tirar_datos():
    return random.randint(3,13)

def pedir_respuestas():
    print("Ingresa tu predicción")
    print("1. par")
    print("2. impar")
    print("3. salir del juego")

    return int( input())

def imprimir_resultado(numero, predicción):
    es_par = numero % 2 == 0
    if es_par and predicción == 1:
        print("Ganaste! Número de los dados:", numero)
    elif not es_par and predicción == 2:
        print("Ganaste! Número de los dados:", numero)
    else:
        print("Perdiste! Número de los dados:", numero)

while True:
    numero = tirar_datos()
    prediccion = pedir_respuestas()
    if prediccion == 3:
        break
    imprimir_resultado(numero, prediccion) 

print("Gracias por jugar")

#