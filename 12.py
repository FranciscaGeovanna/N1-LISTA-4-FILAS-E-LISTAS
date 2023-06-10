class Item:
    def __init__(self, valor):
        self.valor = valor
        self.anterior = None
        self.next = None

    def __str__(self):
        return str(self.valor)

class ListaEncadeadaDupla:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.size = 0

    def is_empty(self):
        return self.inicio is None

    def inserirInicio(self, valor):
        novoItem = Item(valor)
        if self.is_empty():
            self.inicio = novoItem
            self.fim = novoItem
        else:
            novoItem.next = self.inicio
            self.inicio.anterior = novoItem
            self.inicio = novoItem
        self.size += 1

    def inserirFinal(self, valor):
        novoItem = Item(valor)
        if self.is_empty():
            self.inicio = novoItem
            self.fim = novoItem
        else:
            novoItem.anterior = self.fim
            self.fim.next = novoItem
            self.fim = novoItem
        self.size += 1

    def removerInicio(self):
        if self.is_empty():
            raise Exception("A lista está vazia")

        if self.inicio == self.fim:
            self.inicio = None
            self.fim = None
        else:
            self.inicio = self.inicio.next
            self.inicio.anterior = None
        self.size -= 1

    def removerFinal(self):
        if self.is_empty():
            raise Exception("A lista está vazia")

        if self.inicio == self.fim:
            self.inicio = None
            self.fim = None
        else:
            self.fim = self.fim.anterior
            self.fim.next = None
        self.size -= 1

    def exibirListaDupla(self):
        if self.is_empty():
            print("A lista está vazia")
        else:
            atual = self.inicio
            while atual is not None:
                print(atual)
                atual = atual.next
            
    def pesquisar(self, nome):
        if self.is_empty():
            raise Exception("A lista está vazia.")
        atual = self.inicio
        while atual is not None:
            if atual.valor[0] == nome:
                return atual.valor[1]
            atual = atual.next
        return False

lista = ListaEncadeadaDupla()

while True:
    print("\n\t OPÇÕES: ")
    print("1 - Adicionar pessoa")
    print("2 - Remover pessoa")
    print("3 - Pesquisar pessoa")
    print("0 - Fechar lista telefônica")

    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        quant = int(input("\nQuantas pessoas deseja adicionar? "))
        for i in range(quant):
            nome = input(f"Digite o nome da {i+1}° pessoa: ")
            telefone = int(input("Informe o número de telefone: "))
            lista.inserirFinal((nome, telefone))
            print("\n\t A pessoa foi adicionada!\n")
        print("Sua lista telefônica: ")
        lista.exibirListaDupla()
    
    elif opcao == 2:
        if lista.is_empty():
            print("\nA lista está vazia.")
        else:
            contato = input("\nInforme o nome da pessoa que deseja remover: ")
            acharRemov = lista.pesquisar(contato) 
            if acharRemov:
                lista.removerInicio()
                print("Contato removido!\n")
                lista.exibirListaDupla()
            else:
                print("\nA pessoa não foi encontrada")
    
    elif opcao == 3:
        if lista.is_empty():
            print("\nA lista está vazia.")
        else:
            nome = input("\nQual nome da pessoa que deseja encontrar? ")
            achar = lista.pesquisar(nome)
        
            if achar:
                print("\nPessoa encontrada!")
                print(f"Nome: {nome}, contato: {achar}")
            else:
                print("\nA pessoa não foi encontrada")
            
    elif opcao == 0:
        print("\nFechando lista telefônica...")
        break
    else:
        print("\nEssa opção não é válida, tente novamente...")
