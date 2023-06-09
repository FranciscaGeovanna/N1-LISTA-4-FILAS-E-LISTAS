class Item:
    def __init__(self, value):
        self.value = value
        self.next = None

class ListaEncadeada:
    def __init__(self):
        self.head = None

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
    
    def insereInicio(self, value):
        novoItem = Item(value)
        novoItem.next = self.head
        self.head = novoItem
    
    def removeInicio(self):
        if self.is_empty():
            raise IndexError("A fila está vazia.")
        else:
            self.head = self.head.next
    
    def removeFinal(self):
        if self.is_empty():
            raise IndexError("A fila está vazia.")
        elif self.head.next is None:
            value = self.head.value
            self.head = None
        else:
            atual = self.head
            anterior = None 
            while atual.next is not None:
                anterior = atual
                atual = atual.next
            anterior.next = None
            return atual.value
        
    def exibirLista(self):
        if self.is_empty():
            print("A lista está vazia.")
            return None
        else:
            atual = self.head
            while atual is not None:
                print(atual.value)
                if atual.next is None:
                    return atual.value
                atual = atual.next

print("Mostra uma lista de números ao contrário\n")

lista = ListaEncadeada()

quant = int(input("Quantos números deseja adicionar a lista? "))
for i in range(quant):
    num = int(input(f"Digite o {i+1}° número: "))
    lista.insereInicio(num)

print("\nLista invertida: ")
lista.exibirLista()
