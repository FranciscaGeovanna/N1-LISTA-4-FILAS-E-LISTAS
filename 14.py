print("Mostra núemros na ordem crescente\n")

class Item:
    def __init__(self, valor):
        self.valor = valor
        self.anterior = None
        self.next = None

    def __str__(self):
        return str(self.valor)
    
class ListaCircular:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.size = 0
    
    def exibirListaCircular(self):
        if self.inicio is None:
            raise Exception("A lista está vazia")

        atual = self.inicio
        print(atual)
        while atual is not self.fim: # agora precisa percorrer a lista até encontrar a cauda, pois não há mais nenhum apontador para None
            print(atual.next)
            atual = atual.next

    def inserirInicio(self, valor):
        novoItem = Item(valor)
        if self.inicio is None:
            self.inicio = self.fim = novoItem
        else:        
            novoItem.next = self.inicio
            self.inicio.anterior = novoItem
            self.inicio = novoItem
            novoItem.next.anterior = novoItem
            self.fim.next= self.inicio

    def inserirFinal(self, valor):
        novoItem = Item(valor)
        if self.inicio is None:
            self.inicio = self.fim = novoItem
        else:
            novoItem.anterior = self.fim
            self.fim.next = novoItem
            self.fim = novoItem
            self.fim.next = self.inicio
            self.inicio.anterior = self.fim

    def removerInicio(self):
        if self.inicio is None:
            raise Exception("A lista está vazia")

        if self.inicio == self.fim:
            self.inicio = self.fim = None
        else:
            self.inicio = self.inicio.next 
            self.inicio.anterior = self.fim # O anterior do inicio agora aponta para o fim
            self.fim.next = self.inicio # O próximo do fim passa a ser o novo inicio

    def removerFinal(self):
        if self.inicio is None:
            raise Exception("A lista está vazia")

        if self.inicio == self.fim:
            self.inicio = None
            self.fim = None
        else:
            self.fim = self.fim.anterior
            self.fim.next = self.inicio
            self.inicio.anterior = self.fim

def ordemAlfabetica():
    # LISTA DE NÚMEROS
    numeros = []
    quant = int(input("Quantos números deseja adicionar a fila? "))
    for i in range(quant):
        num = input(f"Digite o {i+1}° número: ")
        numeros.append(num)
    
    numeros.sort()
    
    # LISTA DUPLA DE NÚMEROS EM ORDEM CRESCENTE
    listaC = ListaCircular()
    for num in numeros:
        listaC.inserirFinal(num)
    
    return listaC

ordem = ordemAlfabetica()

print("\nSua lista em ordem crescente: ")
ordem.exibirListaCircular()