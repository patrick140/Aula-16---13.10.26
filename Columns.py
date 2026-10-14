import pandas as pd

df = pd.read_csv(r"C:\Users\patrick.loureiro\Documents\Aulas\funcionarios.csv")



df["liquido"] = df["lucro"] - df["salario"]


df["nome"] = df['nome'].str.upper()


df['Lucro positivo'] = df['liquido'].apply(lambda x: "Lucro positivo" if x > 0 else "Lucro Negativo")

df = df.rename(columns={'liquido': 'lucro liquido', 'Lucro positivo': 'lucro final'})

print(df)


