import pandas as pd

# Carregar os dados dos arquivos CSV
transacoes = pd.read_csv('Planilhas/transacoes.csv')

# Converter a coluna data_transacao para datetime, permitindo que pandas infira o formato
transacoes['data_transacao'] = pd.to_datetime(transacoes['data_transacao'], errors='coerce')

# Criar a coluna adicional com a data no formato da tabela dim_dates
transacoes['Data'] = transacoes['data_transacao'].dt.strftime('%Y-%m-%d %H:%M:%S%z')

# Exibir as primeiras linhas do dataframe resultante para verificar
print(transacoes.head())

# Salvar a tabela modificada em um novo arquivo CSV, se necessário
transacoes.to_csv('transacoes_modificada.csv', index=False)
