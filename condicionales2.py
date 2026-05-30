print("Escribe tunombre:")
nombre = input()
print("Escribe tu edad")
edad = int(input())

#elif
#Operadores lógicos
#and (y) / or (o)
#and: Todas las expresiones sean True
#or: Con que una de las expresiones sea True
#> <   >=      <=

if nombre == "Yenifer " and edad > 20:
    print("Saluos Yenifer, eres una adulta")
elif nombre == "Yenifer " and edad > 20:
    print("Saludos Yenifer, eres una joven")
else:
    print()

if nombre == "Yenifer" or nombre == "Alejandra":
    print("Me gusta tu nombre")

else:
    print("Que nombre tan rrarro")
    

