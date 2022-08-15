# Implementar a classe de Vetores Não Ordenados

class VetorNaoOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = self.capacidade*[0] 

    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i])

    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print("Capacidade máxima atingida")
        else:
            self.ultima_posicao = self.ultima_posicao + 1
            self.valores[self.ultima_posicao] = valor
    
    def pesquisa(self, valor):
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] == valor:
                return i
        return -1
    
    def excluir(self, valor):
        posicao = self.pesquisa(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
            self.ultima_posicao = self.ultima_posicao - 1
    
    def duplicatas(self, valor):
        duplos = []
        for s in range(self.ultima_posicao +1):
            for y in range(s +1, self.ultima_posicao +1):
                if valor[s] == valor[y]:
                    duplos.append(valor[s])
        return duplos

vetor = VetorNaoOrdenado(8)
# =====================================
# ADICIONEM TESTES A PARTIR DAQUI
# =====================================
vetor.insere(5)
vetor.insere(4)
vetor.insere(7)
vetor.insere(1)
vetor.insere(6)
vetor.insere(4)
vetor.insere(1)
vetor.insere(8)


vetor.imprime()
print( vetor.duplicatas(vetor.valores) )