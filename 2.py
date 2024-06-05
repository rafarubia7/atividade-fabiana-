contador = 0
positivo = 0
negativo = 0
while contador < 20:
    numero = int(input("Digite número inteiro:"))
    if numero > 0:
        positivo += numero
    else:
        negativo += 1
    contador += 1
print(f"A soma dos números positivos é de {positivo}")
print(f"A quantidade de números negativos é de {negativo}")