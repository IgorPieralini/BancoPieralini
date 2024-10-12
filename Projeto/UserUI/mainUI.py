from Projeto.user import user
from Projeto.actions_user import consultar_saldo
from Projeto.actions_user import atualizar_cotacao
from Projeto.actions_user import comprar_cripto
from Projeto.actions_user import consultar_extrato
from Projeto.actions_user import depositar
from Projeto.actions_user import sacar
from Projeto.actions_user import sair
from Projeto.actions_user import vender_cripto

def mainUserInterface():

    logado = False

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

    while True:
       print('1.  Consultar saldo')
       print('2.  Consultar extrato')
       print('3.  Depositar')
       print('4.  Sacar')
       print('5.  Comprar criptomoedas')
       print('6.  Vender criptomoedas')
       print('7.  Atualizar cotação')
       print('8.  Sair')

       user_actions = {
           1: consultar_saldo,
           2: consultar_extrato,
           3: depositar,
           4: sacar,
           5: comprar_cripto,
           6: vender_cripto,
           7: atualizar_cotacao,
           8: sair
       }

       opcao = int(input())

       if opcao == 8:
           break
       if opcao in user_actions:
           user_actions[opcao]
       else:
           print('Valor inválido, tente novamente por gentileza')

