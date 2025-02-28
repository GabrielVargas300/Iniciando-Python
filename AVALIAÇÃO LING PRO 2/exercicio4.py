salario_fixo = float(input("Digite o salário fixo do vendedor: "))
total_vendas = float(input("Digite o total de vendas no mês: "))

if 100 < total_vendas <= 500:
    premio = 500.00
elif 500 < total_vendas <= 750:
    premio = 700.00
elif total_vendas > 750:
    premio = 1000.00
else:
    premio = 0.00

salario_final = salario_fixo + premio

print("\nResumo do Salário:")
print(f"Salário Fixo: R${salario_fixo:.2f}")
print(f"Prêmio: R${premio:.2f}")
print(f"Salário Final: R${salario_final:.2f}")

