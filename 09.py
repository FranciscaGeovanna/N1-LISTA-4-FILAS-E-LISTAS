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
    
    def pesquisar(self, conta):
        if self.is_empty():
            raise Exception("A lista está vazia.")
        atual = self.head
        while atual is not None:
            if atual.value[1] == conta:
                return True
            atual = atual.next
        return False

    def exibirLista(self):
        if self.is_empty():
            print("\nA lista está vazia.")
        else:
            print("\nTABELA DE CLIENTES:")
            print("--------------------------------------------------")
            print("|    Nome    |   Número da Conta   |     Saldo     |")
            print("--------------------------------------------------")
            atual = self.head
            while atual is not None:
                cliente, numConta, saldo = atual.value
                print(f"| {cliente:<10} | {numConta:<18} | {saldo:<14} |") # FORMATAR 
                atual = atual.next
            print("--------------------------------------------------")

lista = ListaEncadeada()

while True:
    print("\n\t OPÇÕES: ")
    print("1 - Adicionar cliente")
    print("2 - Remover cliente")
    print("3 - Pesquisar cliente")
    print("0 - Encerrar programa")

    opcao = (int(input("Escolha uma opção: ")))
    if opcao == 1:
        quant = int(input("\nQuantos clientes deseja adicionar? "))
        for i in range(quant):
            nome = input(f"\nDigite o nome do {i+1}° cliente: ")
            numConta = int(input("Informe o número da conta do cliente: "))
            saldo = float(input("Informe o saldo da conta: "))
            lista.insereFinal((nome, numConta, saldo))
            print("\n\t O cliente foi adicionado!")
        lista.exibirLista() #TABELA
    
    elif opcao == 2:
        if lista.is_empty():
            print("\nA lista está vazia.")
        numConta = int(input("\nInforme o número da conta que deseja remover: "))
        acharRemov = lista.pesquisar(numConta) # Achar cliente pelo número da conta para remover
        if acharRemov:
            lista.removeInicio()
            print("Cliente removido!\n")
            lista.exibirLista() #TABELA
        else:
            print("\nO cliente não foi encontrado")
    
    elif opcao == 3:
        if lista.is_empty():
            print("\nA lista está vazia.")
        else:
            nome = input("\nQual nome do cliente que deseja encontrar? ")
            achar = lista.pesquisar(numConta)
        
            if achar:
                print("\nCliente encontrado!")
                lista.exibirLista() #TABELA
            else:
                print("\nO cliente não foi encontrado")
            
    elif opcao == 0:
        print("Encerrando programa...")
        break
    else:
        print("Essa opção não é válida")
    
    