import requests
cep= input("digite seu cep: ")

# URL da API buscando o CEP da Praça da Sé em SP
url = f"https://viacep.com.br/ws/{cep}/json/"

try:
    # Fazendo a requisição HTTP GET
    resposta = requests.get(url)
    
    # Verificando se a requisição foi bem-sucedida (Status Code 200)
    if resposta.status_code == 200:
        dados = resposta.json()  # Converte o conteúdo para um dicionário Python
        
        print("--- Dados do Endereço ---")
        print(f"Logradouro: {dados.get('logradouro')}")
        print(f"Bairro: {dados.get('bairro')}")
        print(f"Cidade: {dados.get('localidade')} - {dados.get('uf')}")
    else:
        print(f"Erro na requisição. Status: {resposta.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Erro de conexão: {e}")
