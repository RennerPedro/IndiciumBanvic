import pandas as pd

# Leitura do arquivo CSV para um DataFrame do Pandas
df = pd.read_csv('Planilhas/dim_dates.csv')

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

# Calculando o volume de transações por dia da semana
df_volume_dia_semana = df.groupby('Dia da Semana').size().reset_index(name='volume_transacoes')

# Exibindo os volumes por dia da semana
print("Volumes de transações por dia da semana:")
print(df_volume_dia_semana[['Dia da Semana', 'volume_transacoes']])

df_volume_dia_semana.to_csv('volume_dia_semana.csv', index=False)
