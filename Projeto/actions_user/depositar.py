from Projeto.database import loadupload

# deposita valor
def mathdepositar():
    saldo = loadupload.loadatabase()

    deposito = float(input('Digite o valor do depósito: '))
    saldo = saldo + deposito
    loadupload.uploaddatabase(saldo)

    print('O valor na sua carteira é de', saldo)