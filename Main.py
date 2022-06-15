#Sistema de Biblioteca - Equipe: João Vítor Maia, Maxwel Gomes, Gabriel Dext, Raul Braga

#Main
from datetime import timedelta, date
from colorama import Back, Fore, Style

#Classes
class Livro():
    def __init__(self,titulo,autor):
        self.titulo = titulo
        self.autor = autor
        self.disponibilidade = True
        self.devolucao = "---"

class Biblioteca():
    def __init__(self):
        self.livros = []
        self.users = []

    def cadastrarLivro(self,titulo,autor):
        self.livros.append(Livro(titulo,autor))
    
    def cadastrarPessoa(self,nome):
        self.users.append(user(nome))
        
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

#Variáveis de data
dataAtual = date.today()
diffData = timedelta(days = 15)

#Criando objeto Biblioteca (construtor: [Biblioteca(sem parâmetros)])
biblioteca = Biblioteca()

#Execução do programa
print(Fore.CYAN)
print(f'{Fore.RESET + Fore.YELLOW +" SISTEMA DE BIBLIOTECA "+ Fore.RESET + Fore.CYAN:-^148}')
print(Fore.RESET)

while True:
    yesNo = 0
    print(f'{Fore.BLUE}{"Bem-vinde ao sistema de biblioteca!"}{Fore.RESET}')
    biblioteca.cadastrarPessoa(input(Fore.BLUE + "Insira o nome da pessoa a ser cadastrada: "+ Fore.RESET + Fore.MAGENTA))
    print(Fore.RESET)

    biblioteca.cadastrarLivro(input(Fore.BLUE))
    break




