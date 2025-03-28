# Criando o dicionário do aluno
aluno = {
    "nome": "João",
    "idade": 20,
    "curso": "Engenharia",
    "notas": [8.5, 7.0, 9.2]
}

aluno["cidade"] = "São Paulo"

media_notas = sum(aluno["notas"]) / len(aluno["notas"])
print("Média das notas do aluno:", round(media_notas, 2))

if "telefone" in aluno:
    print("O telefone do aluno é:", aluno["telefone"])
else:
    print("A chave 'telefone' não existe no dicionário.")

print("Dicionário atualizado:", aluno)
