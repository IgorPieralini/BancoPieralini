import os

class ConfigUser:
    def __init__(self, user_file):
        self.users = []  # Lista de usuários
        self.selected_user = None  # Armazena o usuário selecionado
        self.user_file = user_file  # Caminho do arquivo de usuários
        self.carregar_usuarios()  # Carrega os usuários do arquivo

    # Função para carregar os usuários do arquivo
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

    # Busca e seleciona um usuário pelo CPF
    def select_user_by_cpf(self, cpf):
        cpf = cpf.strip()
        print(f"[DEBUG] Procurando usuário com CPF: '{cpf}'")

        for user in self.users:
            user_cpf = user['cpf'].strip()
            print(f"[DEBUG] Comparando '{user_cpf}' com '{cpf}'")

            if user_cpf == cpf:
                self.selected_user = user
                print(f"[DEBUG] Usuário {user['name']} selecionado com sucesso.")
                return True

        print(f"[DEBUG] Usuário com CPF '{cpf}' não encontrado.")
        return False

    # Mostra o saldo e as criptomoedas do usuário selecionado
    def mostrar_valores(self):
        if self.selected_user:
            print(f"Saldo: {self.selected_user['saldo']}")
            print(f"Bitcoin: {self.selected_user['bitcoin']}")
            print(f"Ethereum: {self.selected_user['ethereum']}")
            print(f"Ripple: {self.selected_user['ripple']}")
        else:
            print("Nenhum usuário foi selecionado.")

    # Salva as alterações feitas nos usuários
    def salvar_users(self):
        try:
            with open(self.user_file, 'w', encoding='utf-8') as arquivo:
                for user in self.users:
                    linha = f"{user['cpf']},{user['name']},{user['password']},{user['saldo']},{user['bitcoin']},{user['ethereum']},{user['ripple']}\n"
                    arquivo.write(linha)
            print("Usuários salvos com sucesso!")
        except Exception as e:
            print(f"Erro ao salvar usuários: {e}")

    # Propriedades para acessar os valores do usuário selecionado
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