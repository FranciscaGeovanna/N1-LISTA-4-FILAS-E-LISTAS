print("Mostras as palavras com mais de 5 caracteres que foram recebidas\n")

def maisDeCinco(lista):
    palavras = []
    for caractere in lista:
        if len(caractere) > 5:
            palavras.append(caractere)
    return palavras

lista = []
quant = int(input("Quantas palavras deseja adicionar? "))
for i in range(quant):
    strings = input(f"Digite a {i+1}° palavra: ")
    lista.append(strings)

palavras = maisDeCinco(lista)
print("\nPalavra(s) com mais de 5 caracteres: ", palavras)

