import pandas as pd
import numpy as np
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
    # Filtrar canciones del artista
    canciones_artista = df[df['artist'].str.contains(artista, case=False)]

    # Si el artista no está en el dataset
    if canciones_artista.empty:
        print(f"No se encontraron canciones para el artista: {artista}")
        return

    # Eliminar duplicados basados en 'song_title'
    canciones_artista_unicas = canciones_artista.drop_duplicates(subset='song_title')

    # Mostrar las 5 mejores
    mejores_canciones = canciones_artista_unicas.sort_values(by='rank').head(10)

    print(f"Las 5 mejores canciones de {artista} son:\n")
    print(mejores_canciones[['song_title', 'rank', 'artist']])

# Pedir al usuario que seleccione un artista
artista_usuario = input("Ingresa el nombre de un artista que te guste: ")

# Llamado a la función de recomendación
recomendar_canciones_por_artista(artista_usuario)