class Item:
    def __init__(self, value):
        self.value = value
        self.next = None

class ListaEncadeada:
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.head is None
    
    def insereFinal(self, value):
        novoItem = Item(value)
        if self.head is None:
            self.head = novoItem
        else:
            atual = self.head
            while atual.next is not None:
                atual = atual.next
            atual.next = novoItem
        self.size += 1
    
    def insereInicio(self, value):
        novoItem = Item(value)
        novoItem.next = self.head
        self.head = novoItem
        self.size += 1
    
    def removeInicio(self):
        if self.is_empty():
            raise IndexError("A fila está vazia.")
        else:
            self.head = self.head.next
        self.size -= 1
    
    def removeFinal(self):
        if self.is_empty():
            raise IndexError("A fila está vazia.")
        elif self.head.next is None:
            self.head = None
        else:
            atual = self.head
            anterior = None 
            while atual.next is not None:
                anterior = atual
                atual = atual.next
            anterior.next = None
        self.size -= 1
        
    def exibirLista(self):
        if self.is_empty():
            print("A lista está vazia.")
        else:
            atual = self.head
            while atual is not None:
                print(atual.value)
                atual = atual.next
    
        
lista = ListaEncadeada()

lista.insereInicio(3)
lista.insereInicio(2)
lista.insereInicio(1)
lista.insereInicio(0)
lista.insereFinal(4)
lista.insereFinal(5)

lista.exibirLista() # SAÍDA: 0 1 2 3 4 5 

lista.removeInicio()

print("\n")
lista.exibirLista() # SAÍDA: 1 2 3 4 5 

lista.removeFinal()

print("\n")
lista.exibirLista() # SAÍDA: 1 2 3 4
