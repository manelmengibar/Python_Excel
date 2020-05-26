
import pandas as pd

df = pd.read_csv('pokemon_data.csv')

# ----> Nos muestra únicamente los pokemon de tipo Fire. (Solo tenemos en cuenta una columna)

#print(df.loc[df['Type 1'] == "Fire"])

# ----> Nos muestra únicamente los pokemon de tipo Grass y Poison. (Tenemos en cuenta dos columnas)

#print(df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')])

# ----> Nos muestra únicamente los pokemon de tipo Grass y Poison y HP mayor que 70

print(df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)])



# ----> Definimos un nuevo data frame con los valores filtrados y lo guradamos en un fichero csv

new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]

# ----> Reseteamos el index para que no nos muestre las posiciones del fichero csv original

new_df.reset_index(drop=True, inplace=True)

new_df.to_csv('filtered.csv')
