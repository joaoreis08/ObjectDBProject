from biblioteca_db import BibliotecaDB
from models import Usuario, Funcionario, Livro, Emprestimo,Pessoa
from persistent import Persistent
from funcoes import exibir_menu, escolher_opcao



if __name__ == '__main__':
    opcao = exibir_menu()
    escolher_opcao(opcao)
    