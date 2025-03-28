# Criando um conjunto com três cores
cores = {"vermelho", "verde", "amarelo"}

nova_cor = input("Digite uma nova cor para adicionar ao conjunto: ")
cores.add(nova_cor)

cor_remover = input(f"Escolha uma cor para remover {cores}: ")
if cor_remover in cores:
    cores.remove(cor_remover)  
    print(f"A cor '{cor_remover}' foi removida.")
else:
    print(f"A cor '{cor_remover}' não está no conjunto.")

if "azul" in cores:
    print("A cor 'azul' está no conjunto!")
else:
    print("A cor 'azul' não está no conjunto.")

print("Conjunto final de cores:", cores)
