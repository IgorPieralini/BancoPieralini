from Projeto.UserUI.actions_user.consultar_saldo import methconsultar_saldo
from Projeto.UserUI.actions_user.depositar import mathdepositar
from Projeto.UserUI.actions_user.sacar import mathsacar
from Projeto.UserUI.actions_user.comprar_cripto import mathcomprar_cripto
from Projeto.UserUI.actions_user.vender_cripto import mathvender_cripto
from Projeto.UserUI.actions_user.atualizar_cotacao import mathatualizar_cotacao
from Projeto.UserUI.actions_user.sair import mathsair
from Projeto.UserUI.actions_user.ConfigUser import ConfigUser, consultar_extrato

# Inicializa a classe ConfigUser com o caminho para o arquivo de usuários
caminho = 'actions_user/users.txt'
user_config = ConfigUser(caminho)  # Cria uma instância única de ConfigUser

def mainUserInterface():
    """Função principal para login e execução da interface do usuário."""
    logado = False

    # Solicita CPF e senha do usuário
    cpf_user = input('Digite seu CPF: ').strip()
    password_user = input('Digite sua senha: ').strip()

    # Verifica se o CPF e a senha são válidos
    for user in user_config.users:
        if user['cpf'] == cpf_user and user['password'] == password_user:
            print('------------------------------------------------------')
            print(f"Nome: {user['name']}\nCPF: {user['cpf']}\n")
            logado = True

            # Tenta selecionar o usuário pelo CPF
            if not user_config.select_user_by_cpf(cpf_user):
                print("Erro: Não foi possível selecionar o usuário após o login.")
            break

    # Se o login foi bem-sucedido, exibe valores e chama a interface de opções
    if logado:
        print("Login bem-sucedido!")
        user_config.mostrar_valores()  # Exibe os valores do usuário
        executar_interface_usuario(user_config, cpf_user)  # Inicia a interface de opções
    else:
        print("CPF ou senha incorretos. Encerrando programa.")
        exit()

def executar_interface_usuario(user_config, cpf_user):
    """Interface de opções para o usuário logado."""

    # Funções wrapper para cada opção
    def consultar_saldo():
        methconsultar_saldo(user_config, cpf_user)

    def consultar_extrato_opcao():
        consultar_extrato(user_config, cpf_user)  # Passa os parâmetros corretamente

    def depositar():
        mathdepositar(user_config, cpf_user)

    def sacar():
        mathsacar(user_config, cpf_user)

    def comprar_cripto():
        mathcomprar_cripto(user_config, cpf_user, caminho_cotacao)

    def vender_cripto():
        mathvender_cripto(user_config, cpf_user, caminho_cotacao)
    caminho_cotacao =  'actions_user/cotacao'
    def atualizar_cotacao():
        mathatualizar_cotacao(caminho_cotacao)

    def sair():
        print("Sessão encerrada. Até mais!")
        mathsair()

    # Dicionário de opções
    user_options = {
        1: consultar_saldo,
        2: consultar_extrato_opcao,
        3: depositar,
        4: sacar,
        5: comprar_cripto,
        6: vender_cripto,
        7: atualizar_cotacao,
        8: sair
    }

    # Loop para o menu de opções
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
                user_options[opcao]()  # Chama a função correspondente

                if opcao == 8:
                    break  # Encerra o loop e finaliza o programa
            else:
                print('Opção inválida, tente novamente.')

        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
