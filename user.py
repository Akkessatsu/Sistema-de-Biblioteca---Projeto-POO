from Main import dataAtual, diffData

class user():

    #Atributos
    def __init__(self,nome):
        self.nome = nome
        self.livros = []
        self.multa = 0
    
    #Métodos
    def alugar(self,livro):
        livro.status = False
        livro.devolucao = dataAtual + diffData
        self.livros.append(livro)

    