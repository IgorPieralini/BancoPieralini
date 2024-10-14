import os

# localizacao do databse saldos
saldo_local = 'resources/saldo.txt'

# carrega o valor
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

# muda o valor do database
def uploaddatabase(saldo):
    with open(saldo_local, 'w') as arquivo:
        arquivo.write(str(saldo))