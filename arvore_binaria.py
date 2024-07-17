class No_pai:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class Arvore_binaria:
    def __init__(self):
        self.raiz = None

    def cria_no(self, valor):
        return No_pai(valor)

    def adiciona_no(self, valor):
        if self.raiz is None:
            self.raiz = self.cria_no(valor)
        else:
            no_atual = self.raiz
            while True:
                if valor < no_atual.valor:
                    if no_atual.esquerda is None:
                        no_atual.esquerda = self.cria_no(valor)
                        break
                    else:
                        no_atual = no_atual.esquerda
                else:
                    if no_atual.direita is None:
                        no_atual.direita = self.cria_no(valor)
                        break
                    else:
                        no_atual = no_atual.direita

    def em_ordem(self, raiz, resultado=None):
        if resultado is None:
            resultado = []
        if raiz is not None:
            self.em_ordem(raiz.esquerda, resultado)
            resultado.append(raiz.valor)
            self.em_ordem(raiz.direita, resultado)
        return resultado

    def pre_ordem(self, raiz, resultado=None):
        if resultado is None:
            resultado = []
        if raiz is not None:
            resultado.append(raiz.valor)
            self.pre_ordem(raiz.esquerda, resultado)
            self.pre_ordem(raiz.direita, resultado)
        return resultado

    def pos_ordem(self, raiz, resultado=None):
        if resultado is None:
            resultado = []
        if raiz is not None:
            self.pos_ordem(raiz.esquerda, resultado)
            self.pos_ordem(raiz.direita, resultado)
            resultado.append(raiz.valor)
        return resultado

    def exibir_raiz(self):
        if self.raiz is not None:
            print(f"\nNó raiz atual: {self.raiz.valor}")
        else:
            print("A árvore está vazia.")

    def exibir_sequencias(self):
        print(f"\nSequencia em ordem: {self.em_ordem(self.raiz)}")
        print(f"Sequencia em pré-ordem: {self.pre_ordem(self.raiz)}")
        print(f"Sequencia em pós-ordem: {self.pos_ordem(self.raiz)}")

    

arvore_binaria = Arvore_binaria()

# menu do usuário
while True:
    operacao = input("\nDigite o número da operação:\n1. Inserir elemento\n2. Sair\nEscolha: ")
    if operacao == "1":
        valor = int(input("Digite o valor a ser inserido: "))
        arvore_binaria.adiciona_no(valor)
        arvore_binaria.exibir_raiz()
        arvore_binaria.exibir_sequencias()
    elif operacao == "2":
        break
    else:
        print("Opção Inválida, tente novamente")
