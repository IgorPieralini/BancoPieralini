import random as rd

def variacao_5_porcento(valor):
    max_tentativas = 10
    tentativas = 0

    while tentativas < max_tentativas:
        # Gera um fator entre 0.95 e 1.05
        fator = rd.uniform(0.95, 1.05)
        novo_valor = round(valor * fator)

        # Verifica se o valor mudou
        if novo_valor != valor:
            return novo_valor  # Se mudou, retorna o novo valor

        tentativas += 1

    # Caso todas as tentativas falhem, força uma alteração mínima
    return valor + 1 if valor % 2 == 0 else valor - 1

def mathatualizar_cotacao(caminho):
    # Abrir e ler o conteúdo do arquivo original
    with open(caminho, 'r') as arquivo:
        linha = arquivo.readline().strip()  # Ler a linha e remover espaços e quebras de linha

    # Separar os valores e convertê-los para inteiros
    valores = linha.split(',')
    valor1, valor2, valor3 = int(valores[0]), int(valores[1]), int(valores[2])

    # Gerar novos valores com variação de até 5%
    novo_valor1 = variacao_5_porcento(valor1)
    novo_valor2 = variacao_5_porcento(valor2)
    novo_valor3 = variacao_5_porcento(valor3)

    # Exibir os valores para verificação
    print(f"Valor original 1: {valor1}, Novo valor 1: {novo_valor1}")
    print(f"Valor original 2: {valor2}, Novo valor 2: {novo_valor2}")
    print(f"Valor original 3: {valor3}, Novo valor 3: {novo_valor3}")

    # Abrir o arquivo em modo de escrita para sobrescrever os novos valores
    with open(caminho, 'w') as arquivo:
        arquivo.write(f"{novo_valor1},{novo_valor2},{novo_valor3}")

    print("Arquivo sobrescrito com os novos valores.")
