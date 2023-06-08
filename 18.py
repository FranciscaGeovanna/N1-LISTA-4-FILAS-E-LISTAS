print("Mostra os números comuns existentes entre duas listas\n")

def numerosComuns(listaUm, listaDois):
    numeros = []
    for num in listaUm:
        if num in listaDois and num not in numeros:
            print(num)
            numeros.append(num)
    return numeros
            
lista1 = []
lista2 = []
    
quant1 = int(input("Quantos números deseja adicionar na 1° lista? "))
for i in range(quant1):
    numL1 = int(input(f"Digite o {i+1}° número: "))
    lista1.append(numL1)

quant2 = int(input("\nQuantos números deseja adicionar na 2° lista? "))
for j in range(quant2):
    numL2 = int(input(f"Digite o {j+1}° número: "))
    lista2.append(numL2)

print("\nPrimeira lista: ", lista1, "\nSegunda lista: ", lista2)

print("\nNúmeros comuns nas duas listas: ")
mostrar = numerosComuns(lista1, lista2)
