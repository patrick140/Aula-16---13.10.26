import pandas as pd

df1 = pd.read_csv(r"C:\Users\patrick.araujo\Downloads\funcionarios.csv")
df2 = pd.read_csv(r"C:\Users\patrick.araujo\Downloads\funcionarios_v2.csv")


resultado = pd.concat([df1, df2]) #concatena os dois dataframes com indice
resultado = pd.concat([df1, df2], ignore_index=True) #concatena os dois dataframes sem indice

#resultado = pd.concat([df1, df2], axis=1) #concatena os dois dataframes com indice via colunas
#resultado = pd.concat([df1, df2], ignore_index=True, axis=1) #concatena os dois dataframes sem indice via colunas

print(resultado)