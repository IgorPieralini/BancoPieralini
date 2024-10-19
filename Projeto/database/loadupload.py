import os
from calendar import day_abbr

# localizacao do databse saldos
saldo_local = 'resources/saldo.txt'
saldo_bitcoin = 'resources/moedas/bitcoin.txt'
saldo_ethereum = 'resources/moedas/ethereum.txt'
saldo_ripple = 'resources/moedas/ripple.txt'
database_user = 'users.txt'

def loadarquivo(arquivo):
    caminho = arquivo
    if os.path.exists(caminho):
        with open(saldo_local, 'r') as arquivo:
            try:
                # le o database
                return float(arquivo.read())
            except ValueError:
                return 0.0  # Se o valor no arquivo for inválido, retorna 0
    else:
        return 0.0  # Se o arquivo não existir, retorna 0

def uploadarquivo(caminho, saldo):
    with open(caminho, 'w') as arquivo:
        arquivo.write(str(saldo))


def load_users(caminho):

    users = []
    if os.path.exists(caminho):
        try:
            with open(caminho, 'r', encoding='utf-8') as arquivo:
                for linha in arquivo:
                    linha = linha.strip()

                    if linha:
                        dados = linha.split(',')
                        if len(dados) == 3:
                            user = {
                                'cpf': dados[0].strip(),  # Acessa o índice diretamente
                                'name': dados[1].strip(),
                                'password': dados[2].strip()
                            }
                            users.append(user)
        except FileNotFoundError:
            print('O Arquivo não foi encontrado!')

        return users
    else:
        print('ASDADASDASDASD')

def print_users(usuarios):
    """
    Função para imprimir a lista de usuários carregados.
    """
    if not usuarios:
        print("Nenhum usuário encontrado.")
        return

    print("Usuários carregados:")
    print("------------------------------------------------------")
    for user in usuarios:
        print(f"Nome: {user['name']}, CPF: {user['cpf']}, Senha: {user['password']}")
    print("------------------------------------------------------")