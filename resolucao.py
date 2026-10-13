#CRIAR UM DATAFRAME A PARTIR DO ARQUIVO FUNCIONARIOS NULL

#CRIAR UMA VARIAVEL CONTENDO SOMENTE O DATAFRAME COM A LINHAS EM NULO DA COLUNA "DEPARTAMENTO" PREENCHIDAS COM ALGUM VALOR

#CRIAR UMA VARIAVEL CONTENDO SOMENTE O DATAFRAME COM AS LINHAS EM NULO DA COLUNA "LUCRO" REMOVIDAS

import pandas as pd

df = pd.read_csv(r"C:\Users\patrick.araujo\Downloads\funcionarios - Null.csv")

df_dep_preenchido = df.copy()

df_lucro_removido = df.copy()

df_dep_preenchido["departamento"] = df_dep_preenchido["departamento"].fillna("Nenhum")

df_lucro_removido = df_lucro_removido.dropna(subset=['lucro'])

print(df_dep_preenchido)

print("\n")

print(df_lucro_removido)



