soma = 0
contagem = 0

for num in range(101, 500, 2):  # Começa em 101 para incluir 101 e termina em 499
    soma += num
    contagem += 1

media = soma / contagem

print("Soma dos valores ímpares:", soma)
print("Média dos valores ímpares:", media)