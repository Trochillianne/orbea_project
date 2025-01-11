import pandas as pd
import re

def clean_club(club_name):
    """
    Limpia el nombre de un club ciclista según las reglas dadas.

    Args:
        club_name (str): Nombre original del club.

    Returns:
        str: Nombre limpio del club.
    """
    if pd.isna(club_name):
        return 'INDEPENDIENTE'

    # Convertir a mayúsculas
    club_name = club_name.upper()

    # Reemplazar patrones específicos
    patterns_to_remove = [
        'PEÑA CICLISTA', 'PENYA CICLISTA', 'AGRUPACIÓN CICLISTA', 'AGRUPACION CICLISTA',
        'AGRUPACIÓ CICLISTA', 'AGRUPACIO CICLISTA', 'CLUB CICLISTA', 'CLUB'
    ]
    for pattern in patterns_to_remove:
        club_name = re.sub(pattern, '', club_name)

    # Reemplazar prefijos no deseados
    prefix_patterns = [
        r'^C\.C\.', r'^CC', r'^C\.D\.', r'^CD', r'^A\.C\.', r'^AC', r'^A\.D\.', r'^AD',
        r'^A\.E\.', r'^AE', r'^E\.C\.', r'^EC', r'^S\.C\.', r'^SC', r'^S\.D\.', r'^SD'
    ]
    for prefix in prefix_patterns:
        club_name = re.sub(prefix, '', club_name)

    # Reemplazar sufijos no deseados
    suffix_patterns = [
        r'T\.T\.', r'TT', r'T\.E\.', r'TE', r'C\.C\.', r'CC', r'C\.D\.', r'CD',
        r'A\.D\.', r'AD', r'A\.C\.', r'AC'
    ]
    for suffix in suffix_patterns:
        club_name = re.sub(suffix + r'$', '', club_name)

    # Eliminar espacios en blanco extra
    club_name = club_name.strip()

    return club_name if club_name else 'INDEPENDIENTE'

# Aplicar la función al DataFrame
def process_club_data(df):
    """
    Procesa los datos de los clubes ciclistas, limpiando los nombres y agrupando por club.

    Args:
        df (pd.DataFrame): DataFrame original.

    Returns:
        pd.DataFrame: DataFrame con clubes limpios y conteo de ciclistas por club.
    """
    # Crear la columna 'club_clean'
    print("\nLimpiando los nombres de los clubes...")
    df['club_clean'] = df['club'].apply(clean_club)

    # Mostrar los primeros 15 valores
    print("\nPrimeros 15 valores con nombres limpios:")
    print(df[['club', 'club_clean']].head(15))

    # Agrupar por 'club_clean'
    print("\nAgrupando por clubes...")
    club_counts = df['club_clean'].value_counts().reset_index()
    club_counts.columns = ['club_clean', 'count']

    # Ordenar el DataFrame
    club_counts = club_counts.sort_values(by='count', ascending=False)

    print("\nClubes ordenados por número de participantes:")
    print(club_counts.head(10))

    return club_counts

# Suponiendo que el DataFrame ya está cargado como 'dataset'
if __name__ == "__main__":
    # Ruta al dataset
    dataset_path = "data/dataset.csv"

    # Cargar el dataset
    dataset = pd.read_csv(dataset_path, sep=';')

    # Procesar los datos de los clubes
    club_data = process_club_data(dataset)

    # Guardar el resultado
    club_data.to_csv("data/club_data.csv", index=False)
    print("\nDatos de los clubes guardados en 'data/club_data.csv'")