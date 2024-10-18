import os

# localizacao do databse saldos
saldo_local = 'resources/saldo.txt'
saldo_bitcoin = 'resources/moedas/bitcoin.txt'
saldo_ethereum = 'resources/moedas/ethereum.txt'
saldo_ripple = 'resources/moedas/ripple.txt'

def loadarquivo(arquivo):
    caminho = arquivo
    if os.path.exists(caminho):
        with open(saldo_local, 'r') as arquivo:
            try:
                # le o database
                return float(arquivo.read())
            except ValueError:
                return 0.0  # Se o valor no arquivo for inválido, retorna 0
    else:
        return 0.0  # Se o arquivo não existir, retorna 0

def uploadarquivo(caminho, saldo):
    with open(caminho, 'w') as arquivo:
        arquivo.write(str(saldo))