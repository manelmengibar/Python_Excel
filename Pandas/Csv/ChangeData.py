# ----Esconder con (#) las operaciones que no se quieran ejecutar.------

import pandas as pd

df = pd.read_csv('pokemon_data.csv')

# ----> Añadimos una columna cuyo valor va a ser la suma de otras.
# ----> A contiunación hacemos que nos muestre los 5 primeros valores.

df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
print(df.head(5))

# ----> Hacemos lo mismo que que en el comando de arriba.
# ----> Mediante iloc indicamos que selecciones de todas las filas (:) las columnas de la 4  a la 9 ( ponemos 10 ya que siempre es un número más)

#df['Total'] = df.iloc[:, 4:10].sum(axis=1)
#print(df.head(5))

# ----> Con este comando eliminariamos la nueva columna "Total"
# ----> Nos vuelve a mostrar los 5 primeros valores, esta vez sin la columna "Total"

#df = df.drop(columns=['Total'])
#print(df.head(5))


# ----> Modificamos el orden de las columnas solo a la hora de mostrar los valores, no en el fichero origen
cols = list(df.columns.values)
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]
print(df.columns)
