contador = 0
while True:
    numero = float(input("Digite um número: "))
    contador += numero
    if numero == 0:
        break
print(contador)