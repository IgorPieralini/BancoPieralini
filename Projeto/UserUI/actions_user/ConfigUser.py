import os
from datetime import datetime


class ConfigUser:
    def __init__(self, user_file):
        self.users = []
        self.selected_user = None
        self.user_file = user_file
        self.carregar_usuarios()

    def carregar_usuarios(self):
        if os.path.exists(self.user_file):
            try:
                with open(self.user_file, 'r', encoding='utf-8') as arquivo:
                    for linha in arquivo:
                        data = linha.strip().split(',')
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
                            self.users.append(user)
                        else:
                            print('Arquivo mal formatado!')
            except Exception as error:
                print(f"Erro no carregamento de usuários: {error}")
        else:
            print(f"Arquivo {self.user_file} não foi encontrado.")

    def select_user_by_cpf(self, cpf):
        cpf = cpf.strip()
        for user in self.users:
            if user['cpf'].strip() == cpf:
                self.selected_user = user
                print(f"Usuário {user['name']} selecionado com sucesso.")
                return True
        print(f"Usuário com CPF '{cpf}' não encontrado.")
        return False

    def mostrar_valores(self):
        if self.selected_user:
            print(f"Saldo: {self.selected_user['saldo']}")
            print(f"Bitcoin: {self.selected_user['bitcoin']}")
            print(f"Ethereum: {self.selected_user['ethereum']}")
            print(f"Ripple: {self.selected_user['ripple']}")
        else:
            print("Nenhum usuário foi selecionado.")

    def salvar_users(self):
        try:
            with open(self.user_file, 'w', encoding='utf-8') as arquivo:
                for user in self.users:
                    linha = (
                        f"{user['cpf']},{user['name']},{user['password']},{user['saldo']},"
                        f"{user['bitcoin']},{user['ethereum']},{user['ripple']}\n"
                    )
                    arquivo.write(linha)
            print("Usuários salvos com sucesso!")
        except Exception as e:
            print(f"Erro ao salvar usuários: {e}")

    @property
    def saldo(self):
        if self.selected_user:
            return self.selected_user['saldo']
        print("Nenhum usuário foi selecionado.")
        return None

    @property
    def bitcoin(self):
        if self.selected_user:
            return self.selected_user['bitcoin']
        print("Nenhum usuário foi selecionado.")
        return None

    @property
    def ethereum(self):
        if self.selected_user:
            return self.selected_user['ethereum']
        print("Nenhum usuário foi selecionado.")
        return None

    @property
    def ripple(self):
        if self.selected_user:
            return self.selected_user['ripple']
        print("Nenhum usuário foi selecionado.")
        return None


def gerar_extrato(user, valor, moeda, tipo, caminho_arquivo='extrato.txt'):
    data_hora = datetime.now().strftime('%d-%m-%Y %H:%M')
    tipo_operacao = '+' if tipo == 'deposito' else '-'
    linha_extrato = (
        f"{user['cpf']} {data_hora} {tipo_operacao} {valor:.2f} {moeda} "
        f"CT: 0.0 TX: 0.00 "
        f"REAL: {user['saldo']:.2f} BTC: {user.get('bitcoin', 0.0):.3f} "
        f"ETH: {user.get('ethereum', 0.0):.3f} XRP: {user.get('ripple', 0.0):.1f}\n"
    )

    try:
        with open(caminho_arquivo, 'a', encoding='utf-8') as arquivo:
            arquivo.write(linha_extrato)
        print("Extrato atualizado com sucesso.")
    except Exception as e:
        print(f"Erro ao adicionar no extrato: {e}")


def exibir_extrato(user_config):
    if user_config.selected_user:
        consultar_extrato(user_config.selected_user)
    else:
        print("Nenhum usuário selecionado.")


def consultar_extrato(user_config):
    if user_config.selected_user:
        cpf = user_config.selected_user['cpf']
        extrato = usuario_cpf_extrato_por_cpf(cpf)

        if extrato:
            print(f"Extrato do usuário {user_config.selected_user['name']} (CPF: {cpf}):")
            print("------------------------------------------------------")
            for linha in extrato:
                print(linha)
            print("------------------------------------------------------")
        else:
            print(f"Nenhuma transação encontrada para o CPF {cpf}.")
    else:
        print("Nenhum usuário foi selecionado.")


def usuario_cpf_extrato_por_cpf(cpf, caminho_arquivo='actions_user/extrato.txt'):
    extratos_usuario = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                if linha.startswith(cpf):
                    extratos_usuario.append(linha.strip())
    except FileNotFoundError:
        print(f"Arquivo '{caminho_arquivo}' não encontrado.")
    except Exception as e:
        print(f"Erro ao acessar o extrato: {e}")
    return extratos_usuario


def adicionar_extrato(user, valor, tipo, moeda, caminho_arquivo='actions_user/extrato.txt'):
    data_hora = datetime.now().strftime('%d-%m-%Y %H:%M')
    operacao = '+' if tipo == 'compra' else '-'
    linha = (
        f"{user['cpf']} {data_hora} {operacao} {valor:.2f} {moeda} "
        f"CT: 0.0 TX: 0.00 "
        f"REAL: {user['saldo']:.2f} BTC: {user['bitcoin']:.3f} "
        f"ETH: {user['ethereum']:.3f} XRP: {user['ripple']:.1f}\n"
    )

    try:
        with open(caminho_arquivo, 'a', encoding='utf-8') as arquivo:
            arquivo.write(linha)
        print("Transação adicionada ao extrato com sucesso.")
    except Exception as e:
        print(f"Erro ao adicionar transação: {e}")
