from Projeto.actions_user import loadupload
from Projeto.actions_user.loadupload import saldo_local

# saca valores do seu saldo
def mathsacar():
    #pega o saldo atual
    saldo = loadupload.load_arquivos(saldo_local)

    saque = float(input('Digite o valor do saque: '))

    # saldo atual  - valor do saque
    saldo = saldo - saque

    #salva novo saldo
    loadupload.uploadarquivo(saldo_local, saldo)

    print('O valor na sua carteira é de', saldo)