
import pandas as  pd


#Llegim les dades del fitxer mencionat i les guardem a una variable df
df = pd.read_excel('PY.xlsx',)

#Mostrem al terminal els valors de la taula d'excel que s'han guardat a la variable df
print(df.head())
