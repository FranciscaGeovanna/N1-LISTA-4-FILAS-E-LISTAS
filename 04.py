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

print("Mistra uma frase invertida")

string = input("\nDigite uma frase: ")

f = Queue() 

for letra in string:
    f.enqueue(letra)

sInvertida = "" 
while not f.is_empty():
    sInvertida = f.dequeue() + sInvertida

print("Frase invertida:", sInvertida)

if sInvertida == string:
    print("\nA frase é um políndromo!")
else:
    print("\nA frase não é políndromo!")
