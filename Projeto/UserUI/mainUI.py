from Projeto.UserUI.actions_user import consultar_extrato, depositar, sacar, comprar_cripto, vender_cripto, \
    atualizar_cotacao, sair
from Projeto.UserUI.actions_user.consultar_extrato import mathconsultar_extrato
from actions_user.ConfigUser import ConfigUser  # Importe a classe ConfigUser
from Projeto.UserUI.actions_user.consultar_saldo import methconsultar_saldo
from Projeto.UserUI.actions_user.ConfigUser import ConfigUser
from Projeto.UserUI.actions_user.consultar_saldo import methconsultar_saldo
from Projeto.UserUI.actions_user.consultar_extrato import mathconsultar_extrato
from Projeto.UserUI.actions_user.depositar import mathdepositar
from Projeto.UserUI.actions_user.sacar import mathsacar
from Projeto.UserUI.actions_user.comprar_cripto import mathcomprar_cripto
from Projeto.UserUI.actions_user.vender_cripto import mathvender_cripto
from Projeto.UserUI.actions_user.atualizar_cotacao import mathatualizar_cotacao
from Projeto.UserUI.actions_user.sair import mathsair

# Inicializa a classe com o caminho para o arquivo de usuários
caminho = 'actions_user/users.txt'
user_config = ConfigUser(caminho)  # Instância única de ConfigUser

def mainUserInterface():
    """Função principal para o login e execução da interface do usuário."""
    logado = False

    # Solicita CPF e senha do usuário
    cpf_user = input('Digite seu CPF: ').strip()
    password_user = input('Digite sua senha: ').strip()

    # Verifica as credenciais e seleciona o usuário
    for user in user_config.users:
        if isinstance(user, dict) and user['cpf'] == cpf_user and user['password'] == password_user:
            print('------------------------------------------------------')
            print(f"Nome: {user['name']}\nCPF: {user['cpf']}\n")
            logado = True

            # Tenta selecionar o usuário pelo CPF
            if not user_config.select_user_by_cpf(cpf_user):
                print("Erro: Não foi possível selecionar o usuário após o login.")
            break

    # Se o login foi bem-sucedido, exibe os valores e chama a interface de opções
    if logado:
        print("Login bem-sucedido!")
        user_config.mostrar_valores()  # Exibe os valores do usuário
        executar_interface_usuario(user_config, cpf_user)  # Passa a instância correta
    else:
        print("CPF ou senha incorretos. Encerrando programa.")
        exit()

def executar_interface_usuario(user_config, cpf_user):
    """Interface de opções para o usuário logado."""
    caminho = user_config.user_file  # Caminho para o arquivo de usuários

    # Funções wrapper para cada opção
    def consultar_saldo():
        methconsultar_saldo(user_config, cpf_user)

    def consultar_extrato():
        mathconsultar_extrato(user_config, cpf_user)

    def depositar():
        mathdepositar(user_config, cpf_user)

    def sacar():
        mathsacar(user_config, cpf_user)

    def comprar_cripto():
        mathcomprar_cripto(user_config, cpf_user)

    def vender_cripto():
        mathvender_cripto(user_config, cpf_user)

    def atualizar_cotacao():
        mathatualizar_cotacao(user_config, cpf_user)

    def sair():
        mathsair()

    # Dicionário de opções com funções individuais
    user_options = {
        1: consultar_saldo,
        2: consultar_extrato,
        3: depositar,
        4: sacar,
        5: comprar_cripto,
        6: vender_cripto,
        7: atualizar_cotacao,
        8: sair
    }

    while True:
        print('------------------------------------------------------')
        print('1.  Consultar saldo')
        print('2.  Consultar extrato')
        print('3.  Depositar')
        print('4.  Sacar')
        print('5.  Comprar criptomoedas')
        print('6.  Vender criptomoedas')
        print('7.  Atualizar cotação')
        print('8.  Sair')

        try:
            opcao = int(input('Escolha uma opção: '))

            if opcao in user_options:
                # Chama a função correspondente à opção escolhida
                user_options[opcao]()

                if opcao == 8:
                    print("Sessão encerrada. Até mais!")
                    break
            else:
                print('Opção inválida, tente novamente.')

        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
