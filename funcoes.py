from biblioteca_db import BibliotecaDB
from models import Usuario, Funcionario, Livro, Emprestimo,Pessoa
from persistent import Persistent
import sys

# Função para exibir o menu
def exibir_menu():
    print('1 - Usuário')
    print('2 - Funcionário')
    print('3 - Livro')
    print('4 - Empréstimo')
    print('5 - Sair')
    return  int(input('Escolha uma opção: '))

# Função para escolher a opção do menu  
def escolher_opcao(opcao):
    if opcao == 1:
        exibir_menu_usuario()
    elif opcao == 2:
        exibir_menu_funcionario()
    elif opcao == 3:
        exibir_menu_livro()
    elif opcao == 4:
        exibir_menu_emprestimo()
    elif opcao == 5:
        print('Saindo...')
        sys.exit

# Função para exibir o menu do usuário
def exibir_menu_usuario():
    print('1 - Salvar')
    print('2 - Buscar')
    print('3 - Listar')
    opcao = int(input('Escolha uma opção: '))
    if opcao == 1:
        id = input('Informe o id: ')
        nome = input('Informe o nome: ')
        cpf = input('Informe o cpf: ')
        email = input('Informe o email: ')
        numero_cartao = input('Informe o número do cartão: ')
        usuario = Usuario(id, nome, cpf, email, numero_cartao)
        db = BibliotecaDB()
        db.salvar_usuario(usuario)
    elif opcao == 2:
        id = input('Informe o id: ')
        db = BibliotecaDB()
        usuario = db.buscar_usuario(id)
        if usuario:
            print(f'Usuário: {usuario.nome}')
        else:
            print('Usuário não encontrado')
    elif opcao == 3:
        db = BibliotecaDB()
        usuarios = db.listar_usuarios()
        for usuario in usuarios:
            print(f'Usuário: {usuario.nome}')
    voltar_menu()

# Função para exibir o menu do funcionário
def exibir_menu_funcionario():
    print('1 - Salvar')
    print('2 - Buscar')
    print('3 - Buscar por matrícula')
    opcao = int(input('Escolha uma opção: '))
    if opcao == 1:
        id = input('Informe o id: ')
        nome = input('Informe o nome: ')
        cpf = input('Informe o cpf: ')
        email = input('Informe o email: ')
        matricula = input('Informe a matrícula: ')
        cargo = input('Informe o cargo: ')
        funcionario = Funcionario(id, nome, cpf, email, matricula, cargo)
        db = BibliotecaDB()
        db.salvar_funcionario(funcionario)
    elif opcao == 2:
        id = input('Informe o id: ')
        funcionario = BibliotecaDB.buscar_funcionario(id)
        if funcionario:
            print(f'Funcionário: {funcionario.nome}')
        else:
            print('Funcionário não encontrado')
    elif opcao == 3:
        matricula = input('Informe a matrícula: ')
        db = BibliotecaDB()
        funcionario = db.buscar_funcionario_por_matricula(matricula)
        if funcionario:
            print(f'Funcionário: {funcionario.nome}')
        else:
            print('Funcionário não encontrado')
    voltar_menu()

# Função para exibir o menu do livro
def exibir_menu_livro():
    print('1 - Salvar')
    print('2 - Buscar')
    print('3 - Buscar por ISBN')
    opcao = int(input('Escolha uma opção: '))
    if opcao == 1:
        id = input('Informe o id: ')
        titulo = input('Informe o título: ')
        autor = input('Informe o autor: ')
        isbn = input('Informe o ISBN: ')
        livro = Livro(id, titulo, autor, isbn)
        BibliotecaDB.salvar_livro(livro)
    elif opcao == 2:
        id = input('Informe o id: ')
        livro = BibliotecaDB.buscar_livro(id)
        if livro:
            print(f'Livro: {livro.titulo}')
        else:
            print('Livro não encontrado')
    elif opcao == 3:
        isbn = input('Informe o ISBN: ')
        db = BibliotecaDB()
        livro = db.buscar_livro_por_isbn(isbn)
        if livro:
            print(f'Livro: {livro.titulo}')
        else:
            print('Livro não encontrado')
    voltar_menu()

# Função para exibir o menu do empréstimo
def exibir_menu_emprestimo():
    print('1 - Emprestar')
    print('2 - Devolver')
    opcao = int(input('Escolha uma opção: '))
    if opcao == 1:
        id_usuario = input('Informe o id do usuário: ')
        id_livro = input('Informe o id do livro: ')
        db = BibliotecaDB()
        usuario = db.buscar_usuario(id_usuario)
        livro = db.buscar_livro(id_livro)
        if usuario and livro:
            emprestimo = Emprestimo(Persistent.__next_id__, usuario, livro)
            db.salvar_emprestimo(emprestimo)
        else:
            print('Usuário ou livro não encontrado')
    elif opcao == 2:
        id_emprestimo = input('Informe o id do empréstimo: ')
        db = BibliotecaDB()
        emprestimo = db.buscar_emprestimo(id_emprestimo)
        if emprestimo:
            emprestimo.devolver()
        else:
            print('Empréstimo não encontrado')

    voltar_menu()

# Função para voltar ao menu principal
def voltar_menu():
    opcao = exibir_menu()
    escolher_opcao(opcao)