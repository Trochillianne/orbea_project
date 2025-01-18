import pandas as pd
import re

def clean_club(club_name):
    """
    Limpiamos el nombre de un club ciclista

    Args:
        club_name (str): Nombre original del club

    Returns:
        str: Nombre limpio del club
    """
    if pd.isna(club_name):
        return 'INDEPENDIENTE'

    # Convertimos a mayúsculas
    club_name = club_name.upper()

    # Reemplazamos patrones específicos
    patterns_to_remove = [
        'PEÑA CICLISTA', 'PENYA CICLISTA', 'AGRUPACIÓN CICLISTA', 'AGRUPACION CICLISTA',
        'AGRUPACIÓ CICLISTA', 'AGRUPACIO CICLISTA', 'CLUB CICLISTA', 'CLUB'
    ]
    for pattern in patterns_to_remove:
        club_name = re.sub(pattern, '', club_name)

    # Reemplazamos prefijos no deseados
    prefix_patterns = [
        r'^C\.C\.', r'^CC', r'^C\.D\.', r'^CD', r'^A\.C\.', r'^AC', r'^A\.D\.', r'^AD',
        r'^A\.E\.', r'^AE', r'^E\.C\.', r'^EC', r'^S\.C\.', r'^SC', r'^S\.D\.', r'^SD'
    ]
    for prefix in prefix_patterns:
        club_name = re.sub(prefix, '', club_name)

    # Reemplazamos sufijos no deseados
    suffix_patterns = [
        r'T\.T\.', r'TT', r'T\.E\.', r'TE', r'C\.C\.', r'CC', r'C\.D\.', r'CD',
        r'A\.D\.', r'AD', r'A\.C\.', r'AC'
    ]
    for suffix in suffix_patterns:
        club_name = re.sub(suffix + r'$', '', club_name)

    # Eliminamos espacios en blanco
    club_name = club_name.strip()

    return club_name if club_name else 'INDEPENDIENTE'

# Aplicamos la función al DF
def process_club_data(df):
    """
    Procesamos los datos de los clubes ciclistas, limpiando nombres y agrupándolos por club

    Args:
        df (pd.DataFrame): DF original

    Returns:
        pd.DataFrame: DF con clubes limpios y conteo de ciclistas por club
    """
    # Creamos la columna 'club_clean'
    print("\nLimpiando los nombres de los clubes...")
    df['club_clean'] = df['club'].apply(clean_club)

    # Mostramos los primeros 15 valores
    print("\nPrimeros 15 valores con nombres limpios:")
    print(df[['club', 'club_clean']].head(15))

    # Agrupamos por 'club_clean'
    print("\nAgrupando por clubes...")
    club_counts = df['club_clean'].value_counts().reset_index()
    club_counts.columns = ['club_clean', 'count']

    # Ordenamos el DF
    club_counts = club_counts.sort_values(by='count', ascending=False)

    print("\nClubes ordenados por número de participantes:")
    print(club_counts.head(10))

    return club_counts

# Una vez que el DF está cargado como 'dataset'
if __name__ == "__main__":
    # Ruta al dataset
    dataset_path = "data/dataset.csv"

    # Cargamos el dataset
    dataset = pd.read_csv(dataset_path, sep=';')

    # Procesamos los datos de los clubes
    club_data = process_club_data(dataset)

    # Guardamos el resultado
    club_data.to_csv("data/club_data.csv", index=False)
    print("\nDatos de los clubes guardados en 'data/club_data.csv'")