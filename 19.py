print("Programa para mostrar a palavra mais longa de uma lista\n")

def palavraLonga(palavras):
    palavra = ''
    for plr in palavras:
        if len(plr) > len(palavra):
            palavra = plr
    return palavra

lista = []

quant = int(input("Quantas palavras deseja adicionar a lista? "))
for i in range(quant):
    palavras = input(f"Digite a {i+1}° palavras: ")
    lista.append(palavras)

mostrarPalavraLonga = palavraLonga(lista)
print(f"\n{mostrarPalavraLonga} é a palavra mais longa da sua lista")
