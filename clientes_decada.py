import pandas as pd

# Leitura dos dados dos clientes
clientes_df = pd.read_csv('clientes.csv')  # Substitua pelo caminho correto do seu arquivo CSV

# Convertendo a coluna de data_nascimento para datetime
clientes_df['data_nascimento'] = pd.to_datetime(clientes_df['data_nascimento'])

# Calculando a década de nascimento
clientes_df['decada_nascimento'] = (clientes_df['data_nascimento'].dt.year // 10) * 10

# Agrupando por década de nascimento e contando a quantidade de clientes em cada década
clientes_por_decada = clientes_df.groupby('decada_nascimento').size().reset_index(name='quantidade_clientes')

# Exibindo o resultado de clientes por década de nascimento
print("Clientes por década de nascimento:")
print(clientes_por_decada)
print()

# Salvando o resultado em um arquivo CSV
clientes_por_decada.to_csv('clientes_por_decada.csv', index=False)

# Carregar os dados de transações
transacoes_df = pd.read_csv('transacoes.csv')

# Converter a coluna 'data_transacao' para datetime, se necessário
transacoes_df['data_transacao'] = pd.to_datetime(transacoes_df['data_transacao'], errors='coerce')

# Verificar o tipo de transação
transacoes_df['tipo_transacao'] = transacoes_df['nome_transacao'].str.split(' - ', expand=True)[0]

# Mesclar os dados de transações com os dados de clientes usando a coluna 'num_conta'
transacoes_clientes_df = pd.merge(transacoes_df, clientes_df, left_on='num_conta', right_on='cod_cliente')

# Calcular a década de nascimento
transacoes_clientes_df['decada_nascimento'] = (transacoes_clientes_df['data_nascimento'].dt.year // 10) * 10

# Agrupar por década de nascimento e tipo de transação, contando a quantidade de cada tipo
tipos_transacoes_por_decada = transacoes_clientes_df.groupby(['decada_nascimento', 'tipo_transacao']).size().reset_index(name='quantidade_transacoes')

# Exibir o resultado de tipos de transações por década de nascimento
print("Tipos de transações por década de nascimento:")
print(tipos_transacoes_por_decada[['decada_nascimento', 'tipo_transacao', 'quantidade_transacoes']])


# Salvar o resultado em um arquivo CSV
resultado_csv = 'resultado_transacoes_por_decada.csv'
tipos_transacoes_por_decada.to_csv(resultado_csv, index=False)
print(f"Resultado salvo em {resultado_csv}")