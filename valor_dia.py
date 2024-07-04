import pandas as pd

# Carregar os dados dos arquivos CSV
transacoes = pd.read_csv('transacoes_modificada.csv')

# Remover linhas com datas faltantes para evitar erros na conversão
transacoes = transacoes.dropna(subset=['data_transacao'])

# Converter a coluna data_transacao para datetime
transacoes['data_transacao'] = pd.to_datetime(transacoes['data_transacao'], utc=True)

# Extrair o dia da semana da coluna data_transacao
transacoes['dia_semana'] = transacoes['data_transacao'].dt.day_name()

# Calcular a soma dos valores por dia da semana
soma_por_dia_semana = transacoes.groupby('dia_semana')['valor_transacao'].sum().reset_index()

# Ordenar os dias da semana na ordem correta
dias_ordenados = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
soma_por_dia_semana['dia_semana'] = pd.Categorical(soma_por_dia_semana['dia_semana'], categories=dias_ordenados, ordered=True)
soma_por_dia_semana = soma_por_dia_semana.sort_values('dia_semana')

# Exibir o resultado
print(soma_por_dia_semana)

# Salvar o resultado em um novo arquivo CSV, se necessário
soma_por_dia_semana.to_csv('soma_valores_por_dia_semana.csv', index=False)
