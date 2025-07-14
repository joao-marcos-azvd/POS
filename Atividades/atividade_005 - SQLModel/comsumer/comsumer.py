import requests

url_base = "http://localhost:8000"

try:
    id_pedido = int(input("Digite o ID do pedido que deseja consultar: "))
    resposta = requests.get(f"{url_base}/pedidos/{id_pedido}")
    
    if resposta.status_code == 200:
        print("✅ Pedido encontrado:")
        for chave, valor in resposta.json().items():
            print(f"{chave}: {valor}")
    else:
        print("❌ Pedido não encontrado (erro 404).")

except ValueError:
    print("Digite um ID numérico válido.")
