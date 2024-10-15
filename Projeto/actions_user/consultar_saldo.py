from Projeto.database import loadupload


# consulta o saldo
def methconsultar_saldo():
    # carreg o valor do saldo
    saldo = loadupload.loadatabase()
    bitcoin = loadupload.load_bitcoin()
    ethereum = loadupload.load_ethereum()
    ripple = loadupload.load_ripple()

    print('Reais ', saldo)
    print('Bitcoin: ', bitcoin)
    print('Ethereum: ', ethereum)
    print('Ripple: ', ripple)
