from datetime import datetime

print("***********************************")
print("**         BIENVENIDO  A         **")
print("**      LA TIENDA DE MASCOTAS     **")
print("***********************************")

inventario = {
    "perros": 23,
    "gatos": 20,
    "pajaros": 14,
    "hamster": 5
}

animales_total = 0
for val in inventario.values():
    animales_total += val

print("Por favor ingresa tu nombre")
nombre = input()
print("Por favor escribe tu apelido")
apellido = input()

#Concatenación 
nombre_completo = nombre + "   " + apellido

print("Gracias por visitanos", nombre_completo)

compras = []

def mostrar_menu():
    print("")
    print("===========================")
    print("eleccionar la opcion que deseas:")
    print("1: Conocer cuántos animelestiene la tienda")
    print("2: Comprar un animal")
    print("3 Mostrar compras")
    print("4: Salir del programa")

def mostrar_inventario():
    print("****INVENTARIO****")
    for llave, valor in inventario.items():
        print(f"    {llave}:  {valor}")
    print("En total tenemos", animales_total, "animale")


def comtrar_animal():
    carrito = []

    while True:
        print("¿Que animal desea comprar?  solo puede elegir 1 de cada especie")
        print("Escrbe F para terminar la lista, o V para ver tu carrito")
        animal = input()

        if animal == "F": break

        if animal == "V": 
            print("Tu carrito de compras contiene {carrrito}")
        continue

    if animal not in inventario:
        print(f"Lo sentimos, no contamos con el animal {animal}")
    elif inventario[animal] == 0:
        print(f"Lo sentimos, no tenemos en exixtencia el animal {animal}")
    elif animal not in carrito:
        carrito.append(animal)
    else:
        print("Ese animal ya se encuentra en tu carrito")
        #print("Has comprado un", animal)     
         
    print("El contenido de tucarrito es")
    for animal in carrito:
        print("   ", animal)
        inventario[animal] -= 1
 
    #Agregar esta compra al carrito de compras
    fecha =datetime.now()
    compras.append(  (nombre, carrito, fecha))

def mostras_compras():
    print("")
    print("**** COMPRAS REALIZADAS ****")
for compra in compras:
    print(f"       {compra[0]} compró[1] en {compra[2]}")

while True:
    mostrar_menu()
    respuesta = int(input())

    if respuesta == 1:
        mostrar_inventario()
    elif respuesta == 2:
        comtrar_animal()
    elif respuesta == 3:
        mostras_compras()
    elif respuesta == 4:
        print("Salir del programa")
        break
