from Projeto.database import loadupload
from Projeto.database.loadupload import saldo_local


# deposita valor
def mathdepositar():
    # pega o valor autal
    saldo = loadupload.load_arquivos(saldo_local)

    deposito = float(input('Digite o valor do depósito: '))

    #valor atual + valor deposito
    saldo = saldo + deposito

    #salva o novo valor
    loadupload.upload_arquivos(saldo_local, saldo)

    print('O valor na sua carteira é de', saldo)