'''Escreva um programa que leia uma sequência de números inteiros e insira-os em uma fila até 
que um número negativo seja digitado. Em seguida, remova todos os elementos da fila e exiba-os 
na ordem em que foram inseridos.'''

class Item:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.head is None
    
    def enqueue(self, value):
        novoItem = Item(value)
        if self.is_empty():
            self.head = novoItem
            self.tail = novoItem
        else:
            self.tail.next = novoItem
            self.tail = novoItem
        self.size += 1
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("A fila está vazia.")
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1
        return value    
    
    def get_size(self):
        return self.size
    
def lerEexibir():
    fila = Queue()
    while True:
        num = int(input("Digite um número: "))
        if num >= 0:
            fila.enqueue(num)
        else:
            break 
    
    print("\nNúmeros na ordem em que foram inseridos: ")
    while not fila.is_empty():  
        imprimir = fila.dequeue()
        print(imprimir, end=" ")

print("Adiciona números à fila enquanto não tiver um negativo\n")
lerEexibir()