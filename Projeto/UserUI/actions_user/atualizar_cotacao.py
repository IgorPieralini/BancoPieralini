import random as rd

def variacao_5_porcento(valor):
    max_tentativas = 10
    tentativas = 0

    while tentativas < max_tentativas:
        fator = rd.uniform(0.95, 1.05)
        novo_valor = round(valor * fator)

        if novo_valor != valor:
            return novo_valor  # Se mudou, retorna o novo valor

        tentativas += 1
    return valor + 1 if valor % 2 == 0 else valor - 1

def mathatualizar_cotacao(caminho):
    with open(caminho, 'r') as arquivo:
        linha = arquivo.readline().strip()

    valores = linha.split(',')
    valor1, valor2, valor3 = int(valores[0]), int(valores[1]), int(valores[2])

    novo_valor1 = variacao_5_porcento(valor1)
    novo_valor2 = variacao_5_porcento(valor2)
    novo_valor3 = variacao_5_porcento(valor3)

    print(f"Valor original 1: {valor1}, Novo valor 1: {novo_valor1}")
    print(f"Valor original 2: {valor2}, Novo valor 2: {novo_valor2}")
    print(f"Valor original 3: {valor3}, Novo valor 3: {novo_valor3}")

    with open(caminho, 'w') as arquivo:
        arquivo.write(f"{novo_valor1},{novo_valor2},{novo_valor3}")

    print("Arquivo sobrescrito com os novos valores.")
