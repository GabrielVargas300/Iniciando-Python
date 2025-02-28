dia_nascimento = int(input("Digite o dia de nascimento (DD): "))
mes_nascimento = int(input("Digite o mês de nascimento (MM): "))
ano_nascimento = int(input("Digite o ano de nascimento (AAAA): "))

dia_atual = int(input("Digite o dia atual (DD): "))
mes_atual = int(input("Digite o mês atual (MM): "))
ano_atual = int(input("Digite o ano atual (AAAA): "))

idade = ano_atual - ano_nascimento

if mes_atual < mes_nascimento or (mes_atual == mes_nascimento and dia_atual < dia_nascimento):
    idade -= 1

print("A idade da pessoa é:", idade)

if idade >= 16:
    print("A pessoa tem idade para votar.")
else:
    print("A pessoa não tem idade para votar.")
