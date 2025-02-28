saldo = 0.00

while True:
    print("\n(a) Consulta saldo")
    print("(b) Saque")
    print("(c) Depósito")
    print("(d) Sair")
    
    opcao = input("Opção: ").lower()

    if opcao == 'a':
        print(f"Saldo R${saldo:.2f}")
    
    elif opcao == 'b':
        saque = float(input("Valor: R$"))
        if saque > saldo:
            print("Saldo insuficiente para o saque.")
        else:
            saldo -= saque
            print(f"Saldo R${saldo:.2f}")
    
    elif opcao == 'c':
        deposito = float(input("Valor: R$"))
        saldo += deposito
        print(f"Saldo R${saldo:.2f}")
    
    elif opcao == 'd':
        print("Saindo...")
        break
    
    else:
        print("Opção inválida. Tente novamente.")
