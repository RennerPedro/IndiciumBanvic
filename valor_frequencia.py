import pandas as pd

# Leitura do arquivo CSV com os dados das transações
transacoes = pd.read_csv('Planilhas/transacoes.csv')

# Converter a coluna 'data_transacao' para datetime
transacoes['data_transacao'] = pd.to_datetime(transacoes['data_transacao'], errors='coerce')

# Verificar se houve algum erro na conversão
transacoes = transacoes.dropna(subset=['data_transacao'])

# Identificação dos Tipos de Transações Mais Frequentes e Valores Médios
tipo_transacao = transacoes.groupby('nome_transacao').agg({
    'nome_transacao': 'count',
    'valor_transacao': 'mean'
}).rename(columns={
    'nome_transacao': 'Frequência',
    'valor_transacao': 'Valor Médio'
}).sort_values(by='Frequência', ascending=False)

# Salvar resultado em um arquivo CSV
#tipo_transacao.to_csv('valor_frequencia.csv')

# Visualizar os tipos de transações mais frequentes e valores médios envolvidos
print("Tipos de Transações Mais Frequentes:")
print(tipo_transacao[['Frequência']])

print("\nValores Médios das Transações por Tipo:")
print(tipo_transacao[['Valor Médio']])
