from src.ex1 import load_dataset, display_dataset_info

if __name__ == "__main__":
    # Ruta al dataset
    dataset_path = "data/dataset.csv"

    # Cargar el dataset
    dataset = load_dataset(dataset_path)

    # Mostrar información básica del dataset
    display_dataset_info(dataset)