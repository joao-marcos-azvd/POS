#pip install requests

import requests
# Importando a função que vai listar todos os livros
from ListarTodosLivros import Listar_Todos_Livros
# Importando a função que vai pesquisar um livrom em específico
from PesquisarLivro import Pesquisar_Livro
# Importando a função que vai cadastrar um livrom 
from CadastroLivro import Cadastro_Livro
# Importando a função que vai deletar um livrom em específico
from DeletarLivro import Deletar_Livro
# Importando a função que vai editar o livro 
from EditarLivro import Editar_Livro

if __name__ == "__main__":
    url = "http://127.0.0.1:8000" # URL da API - Tem que tá rodando e não pode ter o "docs" no final
    while True:
        opcao = int(input("""Escolha uma opção
    1 - Listar todos os livros
    2 - Pesquisa livro por título
    3 - Cadastrar um livro
    4 - Deletar um livro
    5 - Editar um livro
    6 - Sair
Opção: """)) 
        #1 - Listar todos os livros
        if opcao == 1:
            # Variável pra armazenar os livros
            todoslivors = Listar_Todos_Livros(url=url) # Passando a url pra a função
            # Aqui eu não preciso usar o if do status_code, pq ele só vai puxar os livros 
            print(todoslivors) # Tem que usar o .text pra só ir a lista com os valores.
            print('')

        #2 - Pesquisa livro por título: peça ao usuário o título para pesquisa    
        elif opcao == 2:
            nome_livro = input('Qual o nome de livro que você deseja: ')
            cadastrado = Pesquisar_Livro(url=url, titulo=nome_livro)
            print(cadastrado)
            print('')

        # 3 - Cadastrar um livro: peça ao usuário os dados do livros e envie o json para cadastrar
        elif opcao == 3: 
            # Aqui é onde eu vou guardar os dados na forma de dicionário pra passar para a API
            dados_livro = {}
            dados_livro['titulo'] = input('Qual livro você deseja cadastrar: ')
            dados_livro['ano'] = int(input('Qual o ano de lançamento do mesmo: '))
            dados_livro['edicao'] = int(input('Qual a edição: '))
            # Aqui eu passo os dados e a url de onde vai ser criado o livro
            livro_cadastrado = Cadastro_Livro(f'{url}/livros', dados_livro) # O erro era pq tava faltando "/livros" no final da url!
            print(livro_cadastrado)
            print('')

        # 4 - Deletar um livro: peça ao usuário o título para deletar
        elif opcao == 4: # Tem um erro aqui! 
            # Pegando o nome do livro que eu desejo apagar
            nome_livro = input('Qual o nome de livro que você deseja deletar: ')
            deletado = Deletar_Livro(url, nome_livro)
            print(deletado)
            print('')

        # 5 - Editar um livro: faça a busca pelo livro e edite os dados dele: Implementa a rota da API e a funcionalidade via requests
        elif opcao == 5:
            titulo_pesquisa = input('Qual o nome de livro que você deseja alterar: ')
            pesquisa = Pesquisar_Livro(url=url, titulo=titulo_pesquisa)
            if pesquisa == 'Livro não encontrado!':
                print(pesquisa)
                print('')

            else:
                novos_dados_livro = {}
                novos_dados_livro['titulo'] = input('Nome: ')
                novos_dados_livro['ano'] = int(input('Ano de lançamento: '))
                novos_dados_livro['edicao'] = int(input('Edição: '))
                editado = Editar_Livro(url=url, titulo=titulo_pesquisa, novos_dados=novos_dados_livro)
                print(editado)
                print('')

        # 6 - SAIR
        elif opcao == 6:
            break 

        else:
            print("Escolha uma opção válida.") 
            print('')   
        