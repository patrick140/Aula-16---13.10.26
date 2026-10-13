import pandas as pd

df = pd.read_csv(r"C:\Users\patrick.araujo\Downloads\funcionarios.csv")

df["liquido"] = df["lucro"] - df["salario"]

df["nome"] = df['nome'].str.upper()

df['Lucro positivo'] = df['liquido'].apply(lambda x: "Lucro positivo" if x > 0 else "Lucro Negativo")

df = df.rename(columns={'liquido': 'lucro liquido'})

print(df)
