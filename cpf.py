import requests

def consultar_cpf(cpf):
    url = f"https://api-production-8163.up.railway.app/api/cpf?cpf={cpf}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Levanta uma exceção para códigos de status HTTP 4xx/5xx
        data = response.json()

        # Exibir as informações retornadas
        print("Consulta realizada com sucesso!")
        print(f"Nome: {data['dadosBasicos']['nome']}")
        print(f"Data de Nascimento: {data['dadosBasicos']['nascimento']}")
        print(f"Nome da Mãe: {data['filiacao']['mae']}")
        
    except requests.exceptions.RequestException as e:
        print("Erro ao consultar o CPF:", e)

# Solicita ao usuário que insira um CPF
cpf_input = input("Digite o CPF (apenas números): ")
if len(cpf_input) == 11 and cpf_input.isdigit():
    consultar_cpf(cpf_input)
else:
    print("CPF inválido. Por favor, insira 11 dígitos numéricos.")
