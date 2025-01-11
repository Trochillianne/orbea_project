from src.ex1 import load_dataset, display_dataset_info
from src.ex2 import name_surname, clean_dataset, get_cyclist_info

if __name__ == "__main__":
    # --- Ejercicio 1: Importación y exploración del dataset ---
    print("\n--- EJERCICIO 1: Importación y exploración del dataset ---")

    # Ruta al dataset
    dataset_path = "data/dataset.csv"

    # Cargamos el dataset
    print("\nCargando el dataset...")
    dataset = load_dataset(dataset_path)

    # Mostramos información básica del dataset
    print("\nMostrando información básica del dataset:")
    display_dataset_info(dataset)

    # --- Ejercicio 2: Anonimización y limpieza del dataset ---
    print("\n--- EJERCICIO 2: Anonimización y limpieza del dataset ---")

    # Verificamos columnas del dataset
    print("\nColumnas del dataset (verificando nombres):")
    print(dataset.columns)

    # Anonimizamos los nombres
    print("\nAnonimizando los nombres en la columna 'biker'...")
    dataset = name_surname(dataset)
    print("\nDataset con nombres anonimizados (primeras 5 filas):")
    print(dataset.head())

    # Limpiamos el dataset eliminando no participantes
    print("\nLimpiando el dataset: Eliminando ciclistas con tiempo '00:00:00'...")
    print(f"Número de registros antes de la limpieza: {dataset.shape[0]}")
    dataset = clean_dataset(dataset)
    print(f"Número de registros después de la limpieza: {dataset.shape[0]}")
    print("\nPrimeras 5 filas después de limpiar el dataset:")
    print(dataset.head())

    # Recuperamos datos del ciclista con dorsal 1000
    print("\nRecuperando información del ciclista con dorsal = 1000...")
    cyclist_data = get_cyclist_info(dataset, 1000)
    if cyclist_data.empty:
        print("No se encontraron datos para el ciclista con dorsal 1000.")
    else:
        print("\nDatos del ciclista con dorsal 1000:")
        print(cyclist_data)