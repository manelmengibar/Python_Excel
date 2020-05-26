
import pandas as pd

df = pd.read_csv('pokemon_data.csv')

# ---->Buscamos los valores en la columna Name que contengan Mega en su nombre.

print(df.loc[df['Name'].str.contains('Mega')])

# ---->Buscamos los valores en la columna Name que empiezen por Pi.

print(df.loc[df['Name'].str.contains('^Pi')])
