#Ciclo,interacion, bucle

#while
""""""
i = 0
while i < 0:
    if i < 6:
        print("El nmero", i, "es menor a 6")
    else:
        print("El numero", i , "es menir o iual a 5")
    i += 1
print("Terminó la interción")
""""""


#for x in "Yenifer":
    #print(x)

while True:
    print("Escribe la opcion deseada")
    print("1: Saludar")
    print("2: Salir")

    respuesta = int(input())

    if respuesta == 1:
        print("Salados chicos!")
    elif respuesta == 2:
        break

print("Terminando programa")
