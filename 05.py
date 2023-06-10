class Item:
    def __init__(self, valor):
        self.valor = valor
        self.next = None

class ListaCircularVetor:
    def __init__(self):
        self.vetor = [] # Vetor para armazenar os itens da lista
        self.inicio = None
        self.fim = None
        self.size = 0

    def vazia(self):
        return self.size == 0
    
    def inserirFinal(self, valor):
        novoItem = Item(valor)
        if self.vazia():
            novoItem.next = novoItem
            self.inicio = novoItem
            self.fim = novoItem
        else:
            novoItem.next = self.inicio
            self.fim.next = novoItem
            self.fim = novoItem
        self.vetor.append(novoItem) # Adiciona o novo item ao vetor
        self.size += 1
    
    def inserirInicio(self, valor):
        novoItem = Item(valor)
        if self.vazia():
            novoItem.next = novoItem
            self.inicio = novoItem
            self.fim = novoItem
        else:
            novoItem.next = self.inicio
            self.inicio = novoItem
            self.fim.next = self.inicio
        self.vetor.append(novoItem)
        self.size += 1
        
    def removerInicio(self):
        if self.vazia():
            raise Exception("A lista está vazia")
        valor = self.inicio
        if self.size == 1:
            self.inicio = None
            self.fim = None
        else:
            self.inicio = self.inicio.next
            self.fim.next = self.inicio
        self.vetor.remove(valor)
        self.size -= 1
        
    def removerFinal(self):
        if self.vazia():
            raise Exception("A lista está vazia!")
        valor = self.fim
        if self.size == 1:
            self.inicio = None
            self.fim = None
        else:
            atual = self.inicio
            while atual.next != self.fim:
                atual = atual.next
            atual.next = self.inicio
            self.fim = atual
        self.vetor.remove(valor)
        self.size -= 1
        
    def exibirListaCircularVetor(self):
        if self.vazia():
            raise Exception("A lista está vazia")
        atual = self.inicio
        while True:
            print(atual.valor)
            atual = atual.next
            if atual == self.inicio:
                break
    
    def pesquisar(self, valor):
        if self.vazia():
            raise Exception("A lista está vazia")
        for item in self.vetor:
            if item.valor == valor:
                return True
        return False


lista = ListaCircularVetor()

lista.inserirInicio(2)
lista.inserirInicio(1)
lista.inserirFinal(3)
lista.inserirFinal(4)

print("Lista: ")
lista.exibirListaCircularVetor() # SAÍDA: 1 2 3 4 

print("\nLista vazia: ", lista.vazia()) # SAÍDA: False

lista.removerInicio()
lista.removerFinal()

print("\nLista atualizada após remover um elemento do início e outro do fim: ")
lista.exibirListaCircularVetor() # SAÍDA: 2 3

print("\nO elemento 2 ainda está na lista? ", lista.pesquisar(2)) # SAÍDA: True

print("\nO elemento 1 ainda está na lista: ", lista.pesquisar(1)) # SAÍDA: False
