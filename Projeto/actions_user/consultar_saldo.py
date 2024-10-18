from Projeto.database import loadupload
from Projeto.database.loadupload import saldo_local, saldo_bitcoin, saldo_ethereum, saldo_ripple


# consulta o saldo
def methconsultar_saldo():
    # carreg o valor do saldo
    saldo = loadupload.loadarquivo(saldo_local)
    bitcoin = loadupload.loadarquivo(saldo_bitcoin)
    ethereum = loadupload.loadarquivo(saldo_ethereum)
    ripple = loadupload.loadarquivo(saldo_ripple)

    print('Reais ', saldo)
    print('Bitcoin: ', bitcoin)
    print('Ethereum: ', ethereum)
    print('Ripple: ', ripple)
