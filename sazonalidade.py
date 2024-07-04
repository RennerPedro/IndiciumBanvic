import pandas as pd

# Carregar os dados das transações, especificando o tratamento de datas e ignorando o fuso horário
transacoes = pd.read_csv('transacoes.csv', parse_dates=['data_transacao'], date_parser=lambda x: pd.to_datetime(x.split()[0]))

# Extrair o mês e o ano da data da transação
transacoes['ano'] = transacoes['data_transacao'].dt.year
transacoes['mes'] = transacoes['data_transacao'].dt.month

# Verificar as primeiras linhas do DataFrame para garantir que a coluna 'categoria_transacao' está presente
print(transacoes.head())

# Agrupar as transações por ano, mês e categoria, e contar o número de transações
volume_transacoes = transacoes.groupby(['ano', 'mes']).size().reset_index(name='volume_transacoes')

# Exibir os primeiros registros para verificação
print(volume_transacoes.head())

# Salvar os resultados em um arquivo CSV
volume_transacoes.to_csv('volume_transacoes_sazonalidade.csv', index=False)

print("Arquivo 'volume_transacoes_sazonalidade.csv' criado com sucesso.")
