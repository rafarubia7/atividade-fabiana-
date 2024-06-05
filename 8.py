def calcular_media_pares():
    numeros = []
    
    while True:
        num = int(input("Digite um número (digite 0 para terminar): "))
        
        if num == 0:
            break
        
        if num % 2 == 0:
            numeros.append(num)
    
    if len(numeros) == 0:
        print("Nenhum número par foi digitado.")
    else:
        media = sum(numeros) / len(numeros)
        print(f"A média dos números pares digitados é: {media}")

calcular_media_pares()