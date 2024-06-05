numero = int(input("Digite o número da tabuada: "))
contador = 0
while contador <= 10:
    tabuada = contador * numero
    print(f"{numero} * {contador} = {tabuada}")
    contador += 1