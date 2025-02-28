#1
numero = int(input("Digite um número inteiro: "))

if (numero % 2 == 0 and numero > 10) or (numero % 2 != 0 and numero < 50):
    print("SIM")
else:
    print("NAO")

#2
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

maior = num1

if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3

print(f"O maior número é: {maior}")

#3
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

numeros = [num1, num2, num3]
numeros.sort()

print(f"Os números em ordem crescente são: {numeros}")

#4
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print(f"Média do aluno: {media:.2f}")

if media >= 6:
    print("Aprovado")
elif media >= 4:
    print("Recuperação")
else:
    print("Reprovado")

5#
numero = int(input("Digite um número inteiro: "))

if numero % 5 == 0 and numero % 3 == 0:
    print(f"{numero} é divisível por 5 e 3 ao mesmo tempo.")
else:
    print(f"{numero} não é divisível por 5 e 3 ao mesmo tempo.")
