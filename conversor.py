print("Bienbenido al conversor de centimetros a metros")

print("Escribe un número en centimetros:")
centimetros = input()

print("Tipo de centimetros", type(centimetros))

centimetros = float(centimetros)
print("Tipo de centimetros", type(centimetros))

# 1 centimetro = 0.01 metros
metros = centimetros * 0.01

print("centimetros ingresado:", centimetros)
print("metros:", metros)