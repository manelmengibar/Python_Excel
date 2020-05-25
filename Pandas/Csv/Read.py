
# ----Esconder con (#) las operaciones que no se quieran ejecutar.------

import pandas as pd

# ----> cargamos la info del csv en una variable df (data frame) que podemos llamar como queramos

df = pd.read_csv('pokemon_data.csv')


# ----> Con este comando (.head(3)) veremos las tres primeras filas de información
# ----> Para ver el listado al completo ejecutariamos lo siguiente "print(df)"

print(df.head(3))

#------------------INFO COLUMNAS-----------------------

# ----> Esto nos muestra los títulos de cada columna.

print(df.columns)

# ----> Una vez leidos los títulos de cada columna, podemos escoger cuales queremos mostrar:

# ----> Muestra los valores de la columna "Name"

print(df['Name'])

# ----> Muestra los valores de varias columnas.

print(df[['Name', 'Attack', 'Speed']][0:5])

# ----> Muestra los valores de 0 a 5 de la columna "Name"

print(df['Name'][0:5])


#------------------INFO FILAS-----------------------

# ----> Muestra la info de la fila 1

print(df.iloc[1])


#------------------POSICIÓN CONCRETA-----------------------

# ----> Muestra valor de fila y columna especificada (en este orden)

print(df.iloc[2,1])
