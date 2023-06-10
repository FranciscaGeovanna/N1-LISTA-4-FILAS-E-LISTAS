class Item:
    def __init__(self, valor):
        self.valor = valor
        self.anterior = None
        self.proximo = None

    def __str__(self):
        return str(self.valor)

class ListaEncadeadaDupla:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def is_empty(self):
        return self.inicio is None

    def inserirInicio(self, valor):
        novoItem = Item(valor)
        if self.is_empty():
            self.inicio = self.fim = novoItem
        else:
            novoItem.proximo = self.inicio
            self.inicio.anterior = novoItem
            self.inicio = novoItem

    def inserirFinal(self, valor):
        novoItem = Item(valor)
        if self.is_empty():
            self.inicio = self.fim = novoItem
        else:
            novoItem.anterior = self.fim
            self.fim.proximo = novoItem
            self.fim = novoItem

    def removerInicio(self):
        if self.is_empty():
            raise Exception("A lista está vazia")

        if self.inicio == self.fim:
            self.inicio = self.fim = None
        else:
            self.inicio = self.inicio.proximo
            self.inicio.anterior = None

    def removerFinal(self):
        if self.is_empty():
            raise Exception("A lista está vazia")

        if self.inicio == self.fim:
            self.inicio = self.fim = None
        else:
            self.fim = self.fim.anterior
            self.fim.proximo = None

    def exibirListaDupla(self):
        if self.is_empty():
            print("A lista está vazia")
        else:
            atual = self.inicio
            while atual is not None:
                print(atual)
                atual = atual.proximo

def ordemAlfabetica():
    # LISTA DE NOMES
    strings = []
    quant = int(input("Quantos nomes deseja adicionar a fila? "))
    for i in range(quant):
        nomes = input(f"Digite o {i+1}° nome: ")
        strings.append(nomes)
    
    strings.sort()
    
    # LISTA DUPLA DE NOMES EM ORDEM ALFABÉTICA
    listaD = ListaEncadeadaDupla()
    for nome in strings:
        listaD.inserirFinal(nome)
    
    return listaD

ordem = ordemAlfabetica()

print("\nSua lista em ordem alfabética: ")
ordem.exibirListaDupla()



