# ----Esconder con (#) las operaciones que no se quieran ejecutar.------

import pandas as pd

# ----> Abrimos el fichero csv.

df = pd.read_csv('pokemon_data.csv')


# ----> Realizamos cambios al fichero original.

df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
cols = list(df.columns.values)
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]

# ----> Guardamos cambios en un fichero csv nuevo. Además le indicamos que borre la columna index.

df.to_csv('modified.csv', index = False)

# ----> O lo podemos guardar en un fichero xlsx.

df.to_excel('modified.xlsx', index = False)
