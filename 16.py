print("Soma números")

def somar(numeros):
    soma = sum(numeros)
    return soma

lista = []
quant = int(input("Quantos números deseja somar? "))
for i in range(quant):
    nums = int(input(f"Digite o {i+1}° número: "))
    lista.append(nums)

print("\nLista: ", lista)

resultado = somar(lista)
print("\nResultado da soma dos números da lista: ", resultado)