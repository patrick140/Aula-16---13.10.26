import pandas as pd

df = pd.read_csv(r"C:\Users\patrick.loureiro\Documents\Aulas\funcionarios.csv")

df = df[df['ativo'] == True]

df["Salario_maior_5000"] = df["salario"].apply(lambda x: "possui" if x > 5000 else "não possui")

df = df.rename(columns={"ativo": "empregado"})

print(df)
