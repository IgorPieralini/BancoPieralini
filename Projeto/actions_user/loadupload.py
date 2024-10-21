import os

# Caminho dos arquivos de saldo e banco de dados
saldo_local = 'resources/saldo.txt'
saldo_bitcoin = 'resources/moedas/bitcoin.txt'
saldo_ethereum = 'resources/moedas/ethereum.txt'
saldo_ripple = 'resources/moedas/ripple.txt'
database_user = 'users.txt'

# Função para carregar saldo dos arquivos
def load_arquivos(arquivo):
    if os.path.exists(arquivo):
        try:
            with open(arquivo, 'r') as arq:
                return float(arq.read().strip())
        except ValueError:
            print(f"Erro ao ler o valor de {arquivo}. Retornando saldo 0.0.")
            return 0.0
    else:
        print(f"Arquivo {arquivo} não encontrado. Retornando saldo 0.0.")
        return 0.0

# Função para salvar saldo nos arquivos
def upload_moedas(caminho, saldo, bitcoin, ethereum, ripple):
    with open(caminho, 'w') as arquivo:
        arquivo.write(f'{saldo} {bitcoin} {ethereum} {ripple}')

# Função para carregar todos os usuários do banco de dados
def load_users(caminho):
    users = []
    if os.path.exists(caminho):
        try:
            with open(caminho, 'r', encoding='utf-8') as arquivo:
                for linha in arquivo:
                    linha = linha.strip()
                    if linha:
                        data = linha.split(',')
                        # Verifica se a linha tem exatamente 7 elementos
                        if len(data) == 7:
                            user = {
                                'cpf': data[0].strip(),
                                'name': data[1].strip(),
                                'password': data[2].strip(),
                                'saldo': float(data[3].strip()),
                                'bitcoin': float(data[4].strip()),
                                'ethereum': float(data[5].strip()),
                                'ripple': float(data[6].strip())
                            }
                            users.append(user)
                        else:
                            print(f"Linha inválida: {linha}")
        except FileNotFoundError:
            print('O arquivo não foi encontrado!')
        except Exception as e:
            print(f"Erro ao carregar usuários: {e}")
    else:
        print('Arquivo inexistente!')

    return users

def save_users(caminho, users):
    with open(caminho, 'w', encoding='utf-8') as arquivo:
        for user in users:
            linha = f"{user['cpf']},{user['name']},{user['password']},{user['saldo']},{user['bitcoin']},{user['ethereum']},{user['ripple']}\n"
            arquivo.write(linha)

# Função para atualizar o saldo ou criptomoedas de um usuário específico
def update_user_data(cpf, saldo=None, bitcoin=None, ethereum=None, ripple=None):
    users = load_users(database_user)  # Carrega os usuários do arquivo
    user_found = False

    for user in users:
        if user['cpf'] == cpf:  # Verifica se é o usuário correto
            user_found = True
            # Atualiza somente os valores que foram passados
            if saldo is not None:
                user['saldo'] = saldo
            if bitcoin is not None:
                user['bitcoin'] = bitcoin
            if ethereum is not None:
                user['ethereum'] = ethereum
            if ripple is not None:
                user['ripple'] = ripple
            print(f"Usuário {user['name']} atualizado com sucesso!")
            break

    if user_found:
        save_users(database_user, users)  # Salva as mudanças no arquivo
    else:
        print("Usuário não encontrado.")


# Função para exibir todos os usuários
def print_users(users):
    if not users:
        print("Nenhum usuário encontrado.")
    else:
        print("Usuários carregados:")
        print("------------------------------------------------------")
        for user in users:
            print(f"Nome: {user['name']}, CPF: {user['cpf']}, Senha: {user['password']}, "
                  f"Saldo: {user['saldo']}, Bitcoin: {user['bitcoin']}, "
                  f"Ethereum: {user['ethereum']}, Ripple: {user['ripple']}")
        print("------------------------------------------------------")