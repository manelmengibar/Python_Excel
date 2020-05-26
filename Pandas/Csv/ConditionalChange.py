import pandas as pd

df = pd.read_csv('pokemon_data.csv')

# ----> Buscamos todos los campos de la columna Type 1 que sean "Fire" y los modificamos por "Flame"

#df.loc[df['Type 1'] == 'Fire' , 'Type 1'] = 'Flame'

# ----> Ahora buscamos los campos de Type 1 que contengan Flame  y los mostramos en el terminal.

#print (df.loc[df['Type 1'] == 'Flame'])

# ----> Si buscamos Fire en la columna Type 1 no encontraremos ningún valor.

#print (df.loc[df['Type 1'] == 'Fire'])

# ----> Buscamos pokemons con valor Speed superior a 90 en la columna Attack y cuando se cumple modificamos los vaores
        #este tenga asignado en las columnas Generation y Legendary por Fucing Fast

df.loc[df['Speed'] > 90 , ['Generation' , 'Legendary']] = 'Fucking Fast'

        #Mostramos los pokemons con Speed mayor a 90 para ver si se han hecho los cambios.

print(df.loc[df['Speed'] > 90 ])
