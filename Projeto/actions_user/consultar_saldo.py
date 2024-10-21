from Projeto.actions_user import loadupload
from Projeto.actions_user.loadupload import database_user


# consulta o saldo
def methconsultar_saldo():
    # Esta parte carrega o valor do saldo
    saldo = loadupload.load_arquivos(database_user)
    bitcoin = loadupload.load_arquivos(database_user)
    ethereum = loadupload.load_arquivos(database_user)
    ripple = loadupload.load_arquivos(database_user)

    # mostra o saldo de cada moeda e o saldo geral
    print('Reais ', )
    print('Bitcoin: ', bitcoin)
    print('Ethereum: ', ethereum)
    print('Ripple: ', ripple)
