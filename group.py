import pandas as pd

df = pd.DataFrame({
    'categoria': ['A', 'B', 'A', 'B', 'A'],
    'vendas': [100, 200, 150, 300, 120],
    'quantidade': [1, 2, 1, 3, 2]
})

# Média de vendas por categoria
df.groupby('categoria')['vendas'].mean()

# Soma por categoria (todas as colunas numéricas)
df.groupby('categoria').sum()

# Agrupar por multiplas colunas
df.groupby(['categoria', 'outra_coluna'])['vendas'].sum()

print(df)

df.groupby('categoria')['vendas'].agg(['sum', 'mean', 'max', 'count'])

# Ou com nomes personalizados
df.groupby('categoria').agg(
    total_vendas=('vendas', 'sum'),
    media_vendas=('vendas', 'mean'),
    qtd_registros=('vendas', 'count')
)





""" df = pd.read_csv(r"")

departamento = df.groupby("departamento").count()
departamento = df.groupby("departamento").mean(numeric_only=True)
departamento = df.groupby("departamento").agg({'salario': ["mean", "max","count","sum"], 'lucro': ["mean", "max","count","sum"]})

print(departamento) """