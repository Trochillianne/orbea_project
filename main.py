from src.ex1 import load_dataset, display_dataset_info
from src.ex2 import name_surname, clean_dataset, get_cyclist_info
from src.ex3 import group_and_plot_times
from src.ex4 import clean_club
from src.ex5 import get_ucsc_cyclists, best_ucsc_cyclist, cyclist_position_and_percentage


if __name__ == "__main__":
    # --- EJERCICIO 1: Importación y exploración del dataset ---
    print("\n--- EJERCICIO 1: Importación y exploración del dataset ---")

    # Ruta al dataset
    dataset_path = "data/dataset.csv"

    # Cargamos el dataset
    print("\nCargando el dataset...")
    dataset = load_dataset(dataset_path)

    # Mostramos información básica del dataset
    print("\nMostrando información básica del dataset:")
    display_dataset_info(dataset)

    # --- EJERCICIO 2: Anonimización y limpieza del dataset ---
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

    # --- EJERCICIO 3: Agrupamiento de los minutos. Histograma ---
    print("\n--- EJERCICIO 3: Agrupamiento de los minutos. Histograma ---")
    print("Agrupando tiempos y generando el histograma...")
    group_and_plot_times(dataset)

    # --- EJERCICIO 4: Clubs ciclistas ---
    print("\n--- EJERCICIO 4: Clubs ciclistas ---")
    print("Limpiando los nombres de los clubes...")

    # Aplicamos la función clean_club y creamos la nueva columna 'club_clean'
    dataset['club_clean'] = dataset['club'].apply(clean_club)

    # Mostramos las primeras 15 filas con la columna 'club_clean'
    print("\nDataset con nombres de clubes limpios (primeras 15 filas):")
    print(dataset[['dorsal', 'biker', 'club', 'club_clean']].head(15))

    # Agrupamos por la columna 'club_clean' y contamos los participantes en cada club
    club_counts = dataset.groupby('club_clean').size().reset_index(name='count')

    # Ordenamos por el número de participantes en orden descendente
    club_counts = club_counts.sort_values(by='count', ascending=False)

    # Mostramos los resultados
    print("\nNúmero de ciclistas por club (ordenado por participantes):")
    print(club_counts)

    # Guardamos los resultados en un archivo CSV
    output_path = "data/club_counts.csv"
    club_counts.to_csv(output_path, index=False)
    print(f"\nResultados guardados en: {output_path}")

    # --- EJERCICIO 5: Unió Ciclista Sant Cugat ---
    print("\n--- EJERCICIO 5: Unió Ciclista Sant Cugat (UCSC) ---")

    # Filtrar los ciclistas de UCSC
    print("\nCiclistas del club UCSC:")
    ucsc_cyclists = get_ucsc_cyclists(dataset)
    print(ucsc_cyclists[['dorsal', 'biker', 'time', 'club_clean']])

    # Encontrar el ciclista con el mejor tiempo
    print("\nCiclista de UCSC con el mejor tiempo:")
    best_cyclist = best_ucsc_cyclist(dataset)
    print(best_cyclist[['dorsal', 'biker', 'time', 'club_clean']])

    # Calcular la posición y porcentaje del mejor ciclista
    print("\nPosición y porcentaje del mejor ciclista de UCSC:")
    position, percentage = cyclist_position_and_percentage(dataset, best_cyclist['dorsal'])
    print(f"Posición: {position} de {len(dataset)}, Porcentaje: {percentage:.2f}%")

