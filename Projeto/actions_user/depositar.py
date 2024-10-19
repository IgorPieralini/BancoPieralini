from Projeto.database import loadupload
from Projeto.database.loadupload import saldo_local


# deposita valor
def mathdepositar():
    saldo = loadupload.loadarquivo(saldo_local)

    deposito = float(input('Digite o valor do depósito: '))
    saldo = saldo + deposito
    loadupload.uploadarquivo(saldo_local, saldo)

    print('O valor na sua carteira é de', saldo)