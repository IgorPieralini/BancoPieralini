from Projeto.database import loadupload
from Projeto.database.loadupload import saldo_local


def mathsacar():
    saldo = loadupload.loadarquivo(saldo_local)

    saque = float(input('Digite o valor do saque: '))
    saldo = saldo - saque
    loadupload.uploadarquivo(saldo_local, saldo)

    print('O valor na sua carteira é de', saldo)