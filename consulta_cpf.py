import requests

def consultar_cpf(cpf):
    url = f"https://api-production-8163.up.railway.app/api/cpf?cpf={cpf}"
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        if dados.get('success'):
            print(f"Nome: {dados['nome']}")
            print(f"Nome da Mãe: {dados['nomeMae']}")
            print(f"Data de Nascimento: {dados['dataNascimento']}")
        else:
            print("CPF não encontrado ou inválido.")
    else:
        print(f"Erro ao consultar API: {response.status_code}")

if __name__ == "__main__":
    cpf = input("Digite o CPF (somente números): ")
    consultar_cpf(cpf)
