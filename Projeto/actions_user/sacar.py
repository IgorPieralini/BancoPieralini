from Projeto.database import loadupload

def mathsacar():
    saldo = loadupload.loadatabase()

    saque = float(input('Digite o valor do saque: '))
    saldo = saldo - saque
    loadupload.uploaddatabase(saldo)

    print('O valor na sua carteira é de', saldo)