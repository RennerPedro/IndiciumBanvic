import pandas as pd
import numpy as np
import locale

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

# Leitura dos arquivos CSV
transacoes = pd.read_csv('Planilhas/transacoes.csv')

# Converter a coluna 'data_transacao' para o formato datetime, tratando diferentes formatos
transacoes['data_transacao'] = pd.to_datetime(transacoes['data_transacao'], errors='coerce')

# Verificar se houve algum erro de conversão
if transacoes['data_transacao'].isna().any():
    # Tentar outro formato
    transacoes['data_transacao'] = pd.to_datetime(transacoes['data_transacao'], format='%Y-%m-%d %H:%M:%S.%f %Z', errors='coerce')

# Se ainda houver valores NaT, podemos removê-los ou tratá-los de outra forma
transacoes = transacoes.dropna(subset=['data_transacao'])

# Criação da dimensão de datas
dim_dates = pd.DataFrame({'Data': pd.date_range(start=transacoes['data_transacao'].min(), end=transacoes['data_transacao'].max())})
dim_dates['Dia da Semana'] = dim_dates['Data'].dt.day_name()
dim_dates['Dia'] = dim_dates['Data'].dt.day
dim_dates['Mês'] = dim_dates['Data'].dt.month
dim_dates['Ano'] = dim_dates['Data'].dt.year
dim_dates['Trimestre'] = dim_dates['Data'].dt.quarter
dim_dates['Período do Mês'] = np.where(dim_dates['Dia'] <= 15, 'Início do Mês', 'Final do Mês')

# Join dos dados com a dimensão de datas
transacoes = transacoes.merge(dim_dates, left_on='data_transacao', right_on='Data')

# Salvar dim_dates como CSV
dim_dates.to_csv('dim_dates.csv', index=False)

# 1. Qual dia da semana tem, em média, maior volume de transações e qual tem, também em média, maior valor movimentado?
volume_por_dia = transacoes.groupby('Dia da Semana').size()
valor_por_dia = transacoes.groupby('Dia da Semana')['valor_transacao'].sum()

dia_maior_volume = volume_por_dia.idxmax()
dia_maior_valor = valor_por_dia.idxmax()

print(f'O dia da semana com maior volume de transações é: {dia_maior_volume}')
print(f'O dia da semana com maior valor movimentado é: {dia_maior_valor}')

# 2. O BanVic tem, em média, os maiores valores movimentados no início ou final de mês?
valor_por_periodo = transacoes.groupby('Período do Mês')['valor_transacao'].sum()
periodo_maior_valor = valor_por_periodo.idxmax()

print(f'O período do mês com maior valor movimentado é: {periodo_maior_valor}')
