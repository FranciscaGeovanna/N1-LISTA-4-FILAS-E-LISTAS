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
    
def opcaoEscolhida(opcao, fila):    
    if opcao == 1:
        quant = int(input("\nQuantos números deseja adicionar na fila? "))
        for i in range(quant):
            num = int(input(f"\nDigite o {i+1}° número: "))
            fila.enqueue(num)
            print("\n\t O número foi adicionado a fila!")
    
    elif opcao == 2:
        if fila.is_empty():
           raise Exception ("A pilha está vazia!")
        numRemovido = fila.dequeue()
        print(f"\nO número {numRemovido} foi removido da fila")
    
    elif opcao == 3:
        tam = fila.get_size()
        print("\nO tamanho da fila é: ", tam)
    
    elif opcao == 4:
        if fila.is_empty():
            print("A fila está vazia, adicione números a fila primeiro")
        else:
            print("\nFila:")
            while not fila.is_empty():
                imprimir = fila.dequeue()
                print(imprimir, end = "  ")
                        
    elif opcao == 5:
        exit()
    else:
        print("A opção digitada é inválida, por favor tente novamente")

f = Queue()

while True:
    print("\n\t OPÇÕES: ")
    print("1 - Adicionar número à fila")
    print("2 - Remover número da fila")
    print("3 - Tamanho da fila")
    print("4 - Mostrar fila")
    print("5 - Encerrar programa")

    escolher = int(input("\nEscolha uma opção: "))
    opcaoEscolhida(escolher, f)