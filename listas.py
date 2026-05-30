nombres =["Yenifer", "Daysi", "Karla", "José"]
print(nombres)
#f-strings
for i , nombre in enumerate(nombres):
    #print("se escribió", i, "en la lista:",i, nombre)
    print(f"se escribió {nombre} en la lista con índice (í)")

print("Bienvenidos a la fiesta", nombres[:3])
print("Lo sentimos", nombres[3:])
