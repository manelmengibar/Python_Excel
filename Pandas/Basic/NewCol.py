import pandas as  pd


#Llegim les dades del fitxer mencionat i les guardem a una variable df
df = pd.read_excel('PY.xlsx',)

#Afegim una nova columna per afegir l'edat dels treballadors.
df['Edat'] = 0

#Mostrem al terminal els valors de la taula d'excel que s'han guardat a la variable df
print(df.head())


#Finalment afegim la taula amb la nova columna "edat" en un nou fitxer anomenat NEW_PY.
writer = pd.ExcelWriter('NEW_PY.xlsx')
df.to_excel(writer, 'new_sheet')
writer.save()
