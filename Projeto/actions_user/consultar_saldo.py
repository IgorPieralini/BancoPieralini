from Projeto.database import loadupload
from Projeto.database.loadupload import saldo_local, saldo_bitcoin, saldo_ethereum, saldo_ripple


# consulta o saldo
def methconsultar_saldo():
    # Esta parte carrega o valor do saldo
    saldo = loadupload.load_arquivos(saldo_local)
    bitcoin = loadupload.load_arquivos(saldo_bitcoin)
    ethereum = loadupload.load_arquivos(saldo_ethereum)
    ripple = loadupload.load_arquivos(saldo_ripple)

    # mostra o saldo de cada moeda e o saldo geral
    print('Reais ', saldo)
    print('Bitcoin: ', bitcoin)
    print('Ethereum: ', ethereum)
    print('Ripple: ', ripple)
