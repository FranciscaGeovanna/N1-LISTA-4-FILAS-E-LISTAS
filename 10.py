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


lista = ListaEncadeadaDupla()

lista.inserirFinal(1)
lista.inserirFinal(2)
lista.inserirFinal(3)
lista.inserirFinal(4)
lista.inserirInicio(0)

print("Lista:")
lista.exibirListaDupla()  # SAÍDA: 0 1 2 3 4

print("\n")

lista.removerFinal()

print("Lista atualizada depois de remover o elemento do fim: ")
lista.exibirListaDupla()  # SAÍDA: 0 1 2 3

print("\n")

lista.removerInicio()

print("Lista atualizada depois de remover o elemento do inicio: ")
lista.exibirListaDupla()  # SAÍDA: 1 2 3
