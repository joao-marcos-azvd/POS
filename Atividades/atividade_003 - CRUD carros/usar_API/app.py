import requests

url = "http://127.0.0.1:8000"

def listar():
    req = requests.get(f"{url}/carro")
    print(req.text)
    return req.text

def cadastrar ():
    nome = input('insira o nome do carro : ')
    modelo = input("insira o modelo do carro : ")
    marca = input("digite a marca : ")
    placa = input('digite uma placa :')

    carro = {"nome": nome,"modelo": modelo, "marca": marca, "placa": placa}

    req = requests.post(f'{url}/carro', json = carro)

def pesquisar():
    placa = input('insira o nome do placa : ')
    req = requests.get(f"{url}/carro/{placa}")
    return req.text

def deletar():
    placa = input('insira o nome do placa : ')
    req = requests.delete(f"{url}/carro/{placa}")
    return req.text

def editar():
    placa = input('insira a placa do carro que deseja editar: ')
    n_nome = input('insira o nome do carro : ')
    n_modelo = input("insira o modelo do carro : ")
    n_marca = input("digite a marca : ")

    n_carro = {"nome": n_nome,"modelo": n_modelo, "marca": n_marca }
    req = requests.put(f"{url}/carro/{placa}", json=n_carro)
    

def menu():
    while True:
        print("\n=== MENU carro ===")
        print("1 - Listar carro")
        print("2 - Cadastrar carro")
        print("3 - Pesquisar carro")
        print("4 - Deletar carro")
        print("0 - Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            listar()
        elif escolha == '2':
            cadastrar()
        elif escolha == '3':
            resultado = pesquisar()
            print(resultado)
        elif escolha == '4':
            resultado = deletar()
            print(resultado)
        elif escolha == '0':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()