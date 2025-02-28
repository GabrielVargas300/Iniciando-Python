valor_produto = float(input("Digite o valor do produto: "))
codigo_desconto = int(input("Digite o código de desconto: "))

if codigo_desconto == 33:
    desconto = 10
elif codigo_desconto == 77:
    desconto = 20
elif codigo_desconto == 230 and valor_produto > 100:
    desconto = 30
else:
    desconto = 25

valor_com_desconto = valor_produto * (1 - desconto / 100)

print("\nResumo da Compra:")
print(f"Valor Original: R${valor_produto:.2f}")
print(f"Desconto Aplicado: {desconto}%")
print(f"Valor Final com Desconto: R${valor_com_desconto:.2f}")
