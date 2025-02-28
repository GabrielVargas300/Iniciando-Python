total_soma = 0
contador = 0

while contador < 5:
    numero = float(input(f"Digite o {contador + 1}º número: "))
    total_soma += numero
    contador += 1

print(f"\nA soma dos 5 números é: {total_soma}")
