contador = 0
while contador <= 10:
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    media = (nota1+nota2)/2
    print(f"A média desse aluno é {media}")
    contador += 1