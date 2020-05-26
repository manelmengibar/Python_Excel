
import pandas as pd

df = pd.read_csv('pokemon_data.csv')


# ----> Va a ordenar la columna Name de manera ascendente.

print(df.sort_values('Name' , ascending = True))


# ----> Ordena los valores por tipo y HP de manera descendente (ascending=False)

print(df.sort_values(['Type 1' , 'HP'], ascending=False))
