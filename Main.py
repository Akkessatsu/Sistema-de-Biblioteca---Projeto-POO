#Sistema de Biblioteca - Equipe: João Vítor Maia, Maxwel Gomes, Gabriel Dext, Raul Braga

#Main
from codecs import latin_1_decode
from datetime import datetime, timedelta
import Livro, user, Biblioteca

#Data atual e tempo de aluguel do livro
dataAtual = datetime.date.today()
diffData = timedelta(days = 15)

#Objetos

#Criando os objetos dos livros (construtor: [Livro(titulo,autor)])
"""
L1 = Livro("O Homem de Giz", "C.J. Tudor")
L2 = Livro("Harry Potter e a Pedra Filosofal", "J.K. Rowling")
L3 = Livro("Memórias Póstumas de Brás-Cubas", "Machado de Assis")
L4 = Livro("1984", "George Orwell")         
L5 = Livro("Date a Live Dead-End Tohka", "Kousi Tatibana")

"""

#Criando objeto Biblioteca (construtor: [Biblioteca(sem parâmetros)])
biblioteca = Biblioteca()

while True:

    biblioteca.cadastrar()





