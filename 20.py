def maiorNota(dicionario):
    maiorNota = 0
    for aluno in dicionario:
        nota = aluno['nota']
        if maiorNota is None or nota > maiorNota:
            maior_nota = nota
            aluno = aluno['nome']
    return aluno

print("Mostra o aluno com a maior nota\n")

lista = []

quant = int(input("Quantos alunos deseja adicionar? "))
for i in range(quant):
    dicionario = {}
    chaveNome = input(f"Digite o nome do {i+1}° aluno: ")
    valorNota = int(input("Digite a nota desse aluno: "))
    dicionario['nome'] = chaveNome
    dicionario['nota'] = valorNota
    lista.append(dicionario)

print("\nLista com os alunos e suas notas: ", lista)

aluno = maiorNota(lista)
print("\nAluno com a maior nota: ", aluno)