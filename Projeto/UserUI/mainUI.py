import os

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

    print('------------------------------------------------------')
    print('Nome:', user.nome)
    print('CPF', user.cpf_string)
    print()
    consultar_saldo.methconsultar_saldo()

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

        user_options = {
            1: consultar_saldo.methconsultar_saldo,
            2: consultar_extrato.mathconsultar_extrato,
            3: depositar.mathdepositar,
            4: sacar.mathsacar,
            5: comprar_cripto.mathcomprar_cripto,
            6: vender_cripto.mathvender_cripto,
            7: atualizar_cotacao.mathatualizar_cotacao,
            8: sair.mathsair
        }

        opcao = int(input())

        if opcao in user_options:
            user_options[opcao]()
        else:
            print('Opção inválida, tente novamente por gentileza')

        print('------------------------------------------------------')


