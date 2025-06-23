# pip install requests

import requests

if __name__ == "__main__":
    url = URL_DA_API(GOOGLE)
    r = requests.get(f"{url}/livros")
    print(r.text)
    livro = {
        "titulo": "Python do zero ao avançado",
        "ano": 2025,
        "edição": 1
    }

    r = requests.post(f"{url}/livros", json=livro)
    print(r.status_code)
    print(r.text)

    pesquisa = "livro"
    r = requests.post(f"{url}/livros/{pesquisa}")
    print(r.status_code)
    print(r.text)

    r = requests.delete(url)(f"{url}/livros/{pesquisa}")
    print(r.status_code)