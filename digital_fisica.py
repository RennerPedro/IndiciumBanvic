import pandas as pd

# Carregar os dados das tabelas a partir dos arquivos CSV necessários
agencias = pd.read_csv('agencias.csv')
contas = pd.read_csv('contas.csv')
transacoes = pd.read_csv('transacoes.csv')

# Filtrar as agências digitais e físicas
digital_agencias = agencias[agencias['tipo_agencia'] == 'Digital']['cod_agencia']
fisicas_agencias = agencias[agencias['tipo_agencia'] == 'Física']['cod_agencia']

# Filtrar as transações para as contas associadas às agências digitais e físicas
digital_contas = contas[contas['cod_agencia'].isin(digital_agencias)]['num_conta']
fisicas_contas = contas[contas['cod_agencia'].isin(fisicas_agencias)]['num_conta']

# Contar as transações para cada tipo de agência
digital_transacoes_count = transacoes[transacoes['num_conta'].isin(digital_contas)].shape[0]
fisicas_transacoes_count = transacoes[transacoes['num_conta'].isin(fisicas_contas)].shape[0]

# Exibir os resultados
print(f"Número de transações em agências digitais: {digital_transacoes_count}")
print(f"Número de transações em agências físicas: {fisicas_transacoes_count}")

# Criar um DataFrame com os resultados
resultados = pd.DataFrame({
    'Tipo de Agência': ['Digital', 'Física'],
    'Número de Transações': [digital_transacoes_count, fisicas_transacoes_count]
})

# Salvar os resultados em um arquivo CSV
resultados.to_csv('comparacao_transacoes_agencias.csv', index=False)

print("Arquivo 'comparacao_transacoes_agencias.csv' criado com sucesso.")
