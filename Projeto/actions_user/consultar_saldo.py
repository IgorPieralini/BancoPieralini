from Projeto.database import loadupload

# consulta o saldo
def methconsultar_saldo():
    # carreg o valor do saldo
    saldo = loadupload.loadatabase()

    print('O valor na sua carteira é de', saldo)
