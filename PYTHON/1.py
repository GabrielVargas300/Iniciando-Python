# Criando a tupla com cinco frutas
frutas = ("maçã", "banana", "laranja", "uva", "morango")

print("Primeira fruta:", frutas[0])
print("Última fruta:", frutas[-1])

if "banana" in frutas:
    print("A fruta 'banana' está na tupla!")
else:
    print("A fruta 'banana' não está na tupla.")

nova_tupla = frutas + ("abacaxi",)
print("Nova tupla de frutas:", nova_tupla)