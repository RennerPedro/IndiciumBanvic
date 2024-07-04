import pandas as pd

# Dados fornecidos
data = {
    'Mês': [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12],
    'Trimestre': [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4],
    'Período do Mês': ['Final do Mês', 'Início do Mês', 'Final do Mês', 'Início do Mês',
                       'Final do Mês', 'Início do Mês', 'Final do Mês', 'Início do Mês',
                       'Final do Mês', 'Início do Mês', 'Final do Mês', 'Início do Mês',
                       'Final do Mês', 'Início do Mês', 'Final do Mês', 'Início do Mês',
                       'Final do Mês', 'Início do Mês', 'Final do Mês', 'Início do Mês',
                       'Final do Mês', 'Início do Mês', 'Final do Mês', 'Início do Mês'],
    'volume_transacoes': [192, 194, 161, 180, 208, 195, 195, 195, 208, 195, 195, 195, 208, 195, 208, 195, 195, 195, 208, 195, 195, 195, 208, 195]
}

# Criando DataFrame
df = pd.DataFrame(data)

# Agrupando os dados pela coluna 'Mês', 'Trimestre' e 'Período do Mês' e somando o 'volume_transacoes'
grouped = df.groupby(['Mês', 'Trimestre', 'Período do Mês'])['volume_transacoes'].sum().reset_index()

# Ordenando pela coluna 'Mês' e 'Trimestre' para manter a ordem natural
grouped = grouped.sort_values(by=['Trimestre', 'Mês'])

# Exibindo o DataFrame resultante
print(grouped)
