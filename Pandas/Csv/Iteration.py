
import pandas as pd

df = pd.read_csv('pokemon_data.csv')


#Nos muestra todos los valores de la columna "Name" mediante una iteración.

for index, row in df.iterrows():

    print(index, row['Name'])
