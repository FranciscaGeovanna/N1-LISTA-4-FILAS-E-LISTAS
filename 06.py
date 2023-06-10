import time

class Item:
    def __init__(self, value, id):
        self.value = value
        self.id = id
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.head is None
    
    def enqueue(self, value, id):
        novoItem = Item(value, id)
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
        valor = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1
        return valor.value, valor.id
    
    def get_size(self):
        return self.size
    
fila = Queue()

while True:
    print("\n\t OPÇÕES: ")
    print("1 - Adicionar cliente à fila")
    print("2 - Começar atendimento")
    print("0 - Encerrar atendimento")
    
    escolher = int(input("\nEscolha uma opção: "))
    
    if escolher == 1:
        quant = int(input("\nQuantos clientes deseja adicionar na fila? "))
        for i in range(quant):
            nome = input(f"\nDigite o nome do {i+1}° cliente: ")
            identificacao = int(input("Informe o id do cliente: "))
            fila.enqueue(escolher, identificacao)
            print("\n\t O cliente foi adicionado à fila!")
    
    elif escolher == 2:
        if fila.is_empty():
            raise Exception("A fila está vazia!")
        else:
            print("\nComeçando o atendimento...")
            while not fila.is_empty():
                clienteChamado, identificacao = fila.dequeue()
                print(f"O cliente com o id {identificacao} foi atendido!")
                print("\nChamando próximo cliente...")
                time.sleep(5)
                
            print("Todos os clientes foram atendidos!")

    elif escolher == 0:
        print("\nEncerrando atendimento...")
        exit()
    else:
        print("\nA opção digitada é inválida, por favor tente novamente")