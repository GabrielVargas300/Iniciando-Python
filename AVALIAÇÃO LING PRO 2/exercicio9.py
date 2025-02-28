soma_idades = 0
contador = 0

while True:
    idade = int(input("Digite a idade do indivíduo (ou um número menor ou igual a zero para encerrar): "))
    
    if idade <= 0:
        break
    
    soma_idades = soma_idades + idade
    contador = contador + 1

if contador > 0:
    media = soma_idades / contador
    print("A idade média do grupo é:", media)
else:
    print("Nenhuma idade válida foi inserida.")
