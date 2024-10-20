import os
from calendar import day_abbr

# caminho do arquvio de cada saldo
saldo_local = 'resources/saldo.txt'
saldo_bitcoin = 'resources/moedas/bitcoin.txt'
saldo_ethereum = 'resources/moedas/ethereum.txt'
saldo_ripple = 'resources/moedas/ripple.txt'
database_user = 'users.txt'

def load_arquivos(arquivo):
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

def upload_arquivos(caminho, saldo):
    with open(caminho, 'w') as arquivo: arquivo.write(str(saldo))

# carrega as informações de todos os usários
def load_users(caminho):
    users = []
    # verifica se o arquivo existe
    if os.path.exists(caminho):
        try:
            # abre aqrquivo com codigo utf -8
            with open(caminho, 'r', encoding='utf-8') as arquivo:

                # para cada linha no arquivo
                for linha in arquivo:
                    linha = linha.strip()

                    if linha:
                        data = linha.split(',')
                        if len(data) == 3:
                            # variaveis do usuario
                            user = {
                                'cpf': data[0].strip(),  # Acessa o índice diretamente
                                'name': data[1].strip(),
                                'password': data[2].strip()
                            }
                            users.append(user)
        # se o arquivo nao foi encontrado
        except FileNotFoundError: print('O Arquivo não foi encontrado!')

        return users
    # se o arquivo nao existe
    else:
        print('Arquivo inexistente!')

# mostra todos os usuários
def print_users(users):
    # se nao existe nenhum usuario
    if not users: print("Nenhum usuário encontrado.")

    print("Usuários carregados:")
    print("------------------------------------------------------")

    # para cada user in usuarios
    for user in users: print(f"Nome: {user['name']}, CPF: {user['cpf']}, Senha: {user['password']}")
    print("------------------------------------------------------")