from Projeto.UserUI.mainUI import executar_interface_usuario
from Projeto.UserUI.actions_user.ConfigUser import ConfigUser


def mainUserInterface():
    """Função principal para login e execução da interface do usuário."""

    # Caminho para o arquivo de usuários
    caminho = 'actions_user/users.txt'
    user_config = ConfigUser(caminho)  # Cria a instância de ConfigUser

    # Solicita CPF e senha do usuário
    cpf_user = input('Digite seu CPF: ').strip()
    senha_user = input('Digite sua senha: ').strip()

    # Verifica se o CPF e a senha são válidos
    if user_config.select_user_by_cpf(cpf_user) and user_config.selected_user['password'] == senha_user:
        print(f"Bem-vindo, {user_config.selected_user['name']}!")
        executar_interface_usuario(user_config, cpf_user)  # Passa os argumentos corretamente
    else:
        print("CPF ou senha incorretos. Encerrando programa.")
        exit()


# Início do programa
if __name__ == "__main__":
    mainUserInterface()