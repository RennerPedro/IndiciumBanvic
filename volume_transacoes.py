import pandas as pd

# Leitura do arquivo CSV para um DataFrame do Pandas
df = pd.read_csv('dim_dates.csv')

# Ajuste dos tipos de dados, se necessário
df['Data'] = pd.to_datetime(df['Data'])

# Extraindo informações adicionais de data
df['Dia da Semana'] = df['Data'].dt.day_name()
df['Mes'] = df['Data'].dt.month
df['Trimestre'] = df['Data'].dt.quarter
df['Ano'] = df['Data'].dt.year

# Definindo o período do mês: início (1-15) ou final (16+)
df['Dia do Mes'] = df['Data'].dt.day
df['Periodo do Mes'] = df['Dia do Mes'].apply(lambda x: 'Inicio' if x <= 15 else 'Fim')

# Calculando o volume de transações por mês, trimestre e período do mês
df_volume = df.groupby(['Mes', 'Trimestre', 'Periodo do Mes']).size().reset_index(name='volume_transacoes')

# Ordenando os resultados por mês e trimestre
df_volume = df_volume.sort_values(by=['Mes', 'Trimestre'])

# Calculando a média de transações por dia da semana
media_transacoes_dia_semana = df.groupby('Dia da Semana').size().mean()

# Calculando a média de transações por trimestre
media_transacoes_trimestre = df.groupby('Trimestre').size().mean()

# Comparando o volume de transações no início e no final do mês
inicio_fim_comparacao = df.groupby('Periodo do Mes').size().reset_index(name='volume_transacoes')
periodo_maior_volume = inicio_fim_comparacao.loc[inicio_fim_comparacao['volume_transacoes'].idxmax(), 'Periodo do Mes']

# Dia da semana com maior média de transações
dia_semana_maior_media = df.groupby('Dia da Semana').size().reset_index(name='media_transacoes').sort_values(by='media_transacoes', ascending=False).head(1)

# Trimestre com maior média de transações
trimestre_maior_media = df.groupby('Trimestre').size().reset_index(name='media_transacoes').sort_values(by='media_transacoes', ascending=False).head(1)

# Salvando os resultados em um arquivo CSV
df_volume.to_csv('volume_transacoes_por_mes_trimestre_periodo.csv', index=False)
dia_semana_maior_media.to_csv('dia_semana_maior_media.csv', index=False)
trimestre_maior_media.to_csv('trimestre_maior_media.csv', index=False)
inicio_fim_comparacao.to_csv('inicio_fim_comparacao.csv', index=False)

print("Volume de transações por mês, trimestre e período do mês:")
print(df_volume)
print("\nDia da semana com maior média de transações:")
print(dia_semana_maior_media)
print("\nTrimestre com maior média de transações:")
print(trimestre_maior_media)
print("Período do mês com maior volume de transações:", periodo_maior_volume)
