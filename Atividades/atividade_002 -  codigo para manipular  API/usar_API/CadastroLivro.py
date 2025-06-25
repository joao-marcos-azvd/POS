import requests

# Passando as informações para o cadatsro 
def Cadastro_Livro (url, dados):
    cadastro = requests.post(url, json=dados) # Aqui é a parte do código responsável pelo cadastro das informações
    # Aqui eu vou vê se foi cadastro ou não
    if cadastro.status_code == 200:
        # Foi cadastrado e retorna oque foi cadastrado!
        return ('Livro cadastrado com sucesso!')
    else:
        # Tá dando algum erro, pq tá retornando 404
        return (f"Deu ruim! {cadastro.status_code}") 
