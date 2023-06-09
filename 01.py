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
    
    def elementoFrente(self):
        if self.is_empty():
            raise Exception("A fila está vazia!")
        return self.head.value

# Mostra o primeiro elemento da fila
def elementoDaFrente(fila):
    if fila.is_empty():
        raise Exception("A fila está vazia")
    else:
        frente = fila.dequeue()
        print("O elemento da frente da fila é:", frente)
        return frente

fila = Queue()

for i in range(3):
    num = input("Digite um número: ")
    fila.enqueue(num)

for j in range(3):
    while not fila.is_empty():
        f = elementoDaFrente(fila)
        print("\nRemovendo o elemento ", f)
print("O elemento da frente é None")




