from Projeto.user import user
from Projeto.actions_user import consultar_saldo
from Projeto.actions_user import atualizar_cotacao
from Projeto.actions_user import comprar_cripto
from Projeto.actions_user import consultar_extrato
from Projeto.actions_user import depositar
from Projeto.actions_user import sacar
from Projeto.actions_user import sair
from Projeto.actions_user import vender_cripto


# Interface Principal
def mainUserInterface():
    logado = True

    # se logado tem que logar, se nao abre o programa
    if logado == False:
        print("Bem vindo ao banco Pieralini")
        print()
        cpf_login = int(input("Digite seu CPF: "))

        if cpf_login != user.cpf:
            print('CPF errado, encerrando programa')
            sair.mathsair()

        senha_login = int(input("Digite sua senha: "))

        if senha_login != user.senha:
            print('Senha errada, encerrando programa')
            sair.mathsair()

    # Logaodo, enqaunto o usuario nao quiser sair
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

        opcao = int(input())

        # verficia a opcao
        if opcao == 1:
            consultar_saldo.methconsultar_saldo()
        elif opcao == 2:
            consultar_extrato.mathconsultar_extrato()
        elif opcao == 3:
            depositar.mathdepositar()
        elif opcao == 4:
            sacar.mathsacar()
        elif opcao == 5:
            comprar_cripto.mathcomprar_cripto()
        elif opcao == 6:
            vender_cripto.mathvender_cripto()
        elif opcao == 7:
            atualizar_cotacao.mathatualizar_cotacao()
        elif opcao == 8:
            sair.mathsair()
        else:
            print('Valor inválido, tente novamente por gentileza')
        print('------------------------------------------------------')