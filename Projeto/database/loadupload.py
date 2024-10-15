import os

# localizacao do databse saldos
saldo_local = 'resources/saldo.txt'
saldo_bitcoin = 'resources/moedas/bitcoin.txt'
saldo_ethereum = 'resources/moedas/ethereum.txt'
saldo_ripple = 'resources/moedas/ripple.txt'

# carrega o valor saldo conta
def loadatabase():
    # se o database existe, se nao retorna 0
    if os.path.exists(saldo_local):
        with open(saldo_local, 'r') as arquivo:
            try:
                # le o database
                return float(arquivo.read())
            except ValueError:
                return 0.0  # Se o valor no arquivo for inválido, retorna 0
    else:
        return 0.0  # Se o arquivo não existir, retorna 0

# muda o valor do database saldo conta
def uploaddatabase(saldo):
    with open(saldo_local, 'w') as arquivo:
        arquivo.write(str(saldo))


# CRIPTO BITCOIN
def load_bitcoin():
    # se o database existe, se nao retorna 0
    if os.path.exists(saldo_bitcoin):
        with open(saldo_bitcoin, 'r') as arquivo:
            try:
                # le o database
                return float(arquivo.read())
            except ValueError:
                return 0.0  # Se o valor no arquivo for inválido, retorna 0
    else:
        return 0.0  # Se o arquivo não existir, retorna 0
def upload_bitcoin(saldo):
    with open(saldo_bitcoin, 'w') as arquivo:
        arquivo.write(str(saldo))


# CRIPTO ETHEREUM
def load_ethereum():
    # se o database existe, se nao retorna 0
    if os.path.exists(saldo_ethereum):
        with open(saldo_ethereum, 'r') as arquivo:
            try:
                # le o database
                return float(arquivo.read())
            except ValueError:
                return 0.0  # Se o valor no arquivo for inválido, retorna 0
    else:
        return 0.0  # Se o arquivo não existir, retorna 0
def upload_ethereum(saldo):
    with open(saldo_ethereum, 'w') as arquivo:
        arquivo.write(str(saldo))


# CRIPTO RIPPLE
def load_ripple():
    # se o database existe, se nao retorna 0
    if os.path.exists(saldo_ripple):
        with open(saldo_ripple, 'r') as arquivo:
            try:
                # le o database
                return float(arquivo.read())
            except ValueError:
                return 0.0  # Se o valor no arquivo for inválido, retorna 0
    else:
        return 0.0  # Se o arquivo não existir, retorna 0
def upload_ripple(saldo):
    with open(saldo_ripple, 'w') as arquivo:
        arquivo.write(str(saldo))
