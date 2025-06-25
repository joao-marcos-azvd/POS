# Aqui eu não importo a biblioteca requests pq ela já ta nessa outra
from ListarTodosLivros import Listar_Todos_Livros

# Passando os parametros necessários
def Pesquisar_Livro(url, titulo):
    # pegando todos os livors
    livros = Listar_Todos_Livros(url=url)
    for livro in livros: # Percorendo a lista de dicionários
        if titulo.lower() == livro['titulo'].lower():  # compara ignorando maiúsculas/minúsculas:
            return livro
    # Aqui é pra caso o livor não esteja cadastrado no sistema
    return ('Livro não encontrado!')