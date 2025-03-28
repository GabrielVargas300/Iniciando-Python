# Criando a lista com números de 1 a 10
numeros = list(range(1, 11))

numeros.append(11)

numeros.remove(5)

numeros.reverse()

soma = sum(numeros)

print("Lista após as modificações:", numeros)
print("Soma dos números da lista:", soma)
