from Main import dataAtual, Livro, user

class Biblioteca():
    def __init__(self):
        self.livros = []
        self.users = []

    def cadastrarLivro(self,titulo,autor):
        self.livros.append(Livro(titulo,autor))
    
    def cadastrarPessoa(self,nome):
        self.user.append(user(nome))
        
    def mostrarLivros(self,escolha):
        print(f'{"TÍTULO | AUTOR | Nº EXEMPLAR | DISPONIBILIDADE | DATA DE DEVOLUÇÃO | STATUS"}')
        if escolha == 1:
            for livro in self.livros:
                print(f'{livro.titulo} | {livro.autor} | {livro.exemplar} | {livro.disponibilidade == False: } | {livro.devolucao} | {livro.status}')

        elif escolha == 2:
            for livro in self.livros:
                if livro.disponibilidade == True:
                    print(f'{livro.titulo} | {livro.autor} | {livro.exemplar} | {livro.disponibilidade == False: } | {livro.devolucao} | {livro.status}')
                
                else:
                    continue
        else:
            for livro in self.livros:
                if livro.disponibilidade == False:
                    print(f'{livro.titulo} | {livro.autor} | {livro.exemplar} | {livro.disponibilidade == False: } | {livro.devolucao} | {livro.status}')
                
                else:
                    continue

    def multar(self,user):
        for livro in user.livros:
            if livro.devolucao < dataAtual:
                user.multa += 1.00