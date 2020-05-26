
import pandas as pd

df = pd.read_csv('pokemon_data.csv')


# ----> Esto nos va a mostrar todos las categorias de type 1 que hay y la media de valores de las otras columnas.
    #Por ejemplo: los Pokemon tipo Fire tienen una velocidad media de 48.588235

#print(df.groupby(['Type 1']).mean())

# ----> Podemos hacer que nos muestre todas las medias pero ordenado según los valores de la columna "Attack"
        #De este modo observamos que los de Tipo Dragon son de media los más fuertes  y los tipo Fairy los más débiles

#print(df.groupby(['Type 1']).mean().sort_values('Attack', ascending=False))

# ---->  Creamos una columna nueva y le damos valor 1 a todos los pokemons
        # A continuación utilizamos esta columna para contar cuantos pokemon de cada tipo tenemos  mediante la funcion count()

df['count'] = 1
print(df.groupby(['Type 1']).count()['count'])
