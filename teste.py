import pandas as pd

# Dados
dados = [
    ["Computador 1", "8gb ram", "R$ 2500"],
    ["Computador 2", "16gb ram", "R$ 5500"],
    ["Computador 3", "32gb ram", "R$ 8500"]
]

# Nome da Planilha
nome_planilha = "Meus computadores"

# Nome da página
nome_pagina = "Computadores"

# Nome das colunas
nomes_colunas = ["Eletrônica", "Memória ram", "Preço"]

# Criar um DataFrame com os dados
df = pd.DataFrame(dados, columns=nomes_colunas)

# Criar um arquivo Excel com a planilha
with pd.ExcelWriter(nome_planilha + '.xlsx') as writer:
    df.to_excel(writer, sheet_name=nome_pagina, index=False)

