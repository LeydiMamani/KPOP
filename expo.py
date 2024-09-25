import pandas as pd
import matplotlib.pyplot as plt
file_path = 'C:\\LM\\IA\\kpop ia\\kpop_rankings.csv' 
df = pd.read_csv(file_path) 
# print(df.columns)

# canciones_2020 = df[df['year'] == 2020]
# print(canciones_2020.head(10))

# canciones_2021 = df[df['year'] == 2021]
# print(canciones_2021.head(10))

# canciones_2022 = df[df['year'] == 2022]
# print(canciones_2022.head(10))

# Funcion para recomendar las canciones mejor rankeadas de un artista
def recomendar_canciones_por_artista(artista):
    # Filtra las canciones del artista
    canciones_artista = df[df['artist'].str.contains(artista, case=False)]  # Ignorar mayusculas/minusculas

    # Si el artista no tiene canciones en el dataset
    if canciones_artista.empty:
        print(f"No se encontraron canciones para el artista: {artista}")
        return

    # Ordenar por ranking y mostrar las 5 mejores
    mejores_canciones = canciones_artista.sort_values(by='rank').head(600)

    print(f"Las 5 mejores canciones de {artista} son:\n")
    print(mejores_canciones[['song_title', 'rank']])

# Preguntar al usuario por un artista
artista_usuario = input("Ingresa el nombre de un artista o grupo que te guste: ")

# Llamar a la funcion de recomendaciones
recomendar_canciones_por_artista(artista_usuario)


