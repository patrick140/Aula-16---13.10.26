import pandas as pd

df = pd.read_csv(r"C:\Users\patri\Documents\Documentos Senac\Aulas\Analista de Dados\funcionarios.csv")

df["lucro liquido"] = df["lucro"] - df["salario"]

print(df)
