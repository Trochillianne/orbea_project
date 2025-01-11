import pandas as pd


def load_dataset(filepath):
    """
    Carga el dataset desde un archivo CSV a un DataFrame.

    Args:
        filepath (str): Ruta del archivo CSV.

    Returns:
        pd.DataFrame: DataFrame con los datos cargados.
    """
    try:
        df = pd.read_csv(filepath, sep=';')
        print("Dataset cargado correctamente.")
        return df
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en '{filepath}'.")
        return None


def display_dataset_info(df):
    """
    Muestra información básica del dataset:
    - Las 5 primeras filas.
    - Número de ciclistas participantes.
    - Lista de columnas del dataset.

    Args:
        df (pd.DataFrame): DataFrame a analizar.
    """
    if df is not None:
        print("\nPrimeras 5 filas del dataset:")
        print(df.head())

        print(f"\nNúmero de ciclistas participantes: {df.shape[0]}")

        print("\nColumnas del dataset:")
        print(list(df.columns))
    else:
        print("El DataFrame está vacío o no se cargó correctamente.")