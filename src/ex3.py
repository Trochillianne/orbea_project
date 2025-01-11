import matplotlib.pyplot as plt
import pandas as pd


def minutes_002040(time):
    """
    Redondea los minutos del tiempo a 00, 20 o 40.

    Args:
        time (str): Tiempo en formato 'hh:mm:ss'.

    Returns:
        str: Tiempo con los minutos redondeados, en formato 'hh:mm'.
    """
    hours, minutes, _ = map(int, time.split(':'))
    if minutes < 20:
        minutes = 0
    elif minutes < 40:
        minutes = 20
    else:
        minutes = 40
    return f"{hours:02}:{minutes:02}"


def group_and_plot_times(df, output_path="img/histograma.png"):
    """
    Agrupa los tiempos en franjas de 20 minutos y genera un histograma.

    Args:
        df (pd.DataFrame): DataFrame con los datos, incluyendo la columna 'time'.
        output_path (str): Ruta para guardar el histograma generado.
    """
    # Crear la columna 'time_grouped'
    df['time_grouped'] = df['time'].apply(minutes_002040)

    # Agrupar por 'time_grouped' y contar
    grouped = df.groupby('time_grouped').size().reset_index(name='count')
    print("\nAgrupamiento por tiempos:")
    print(grouped)

    # Crear el histograma
    plt.figure(figsize=(10, 6))
    plt.bar(grouped['time_grouped'], grouped['count'], width=0.4)
    plt.title('Histograma de tiempos agrupados')
    plt.xlabel('Tiempos agrupados (hh:mm)')
    plt.ylabel('Número de ciclistas')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Guardar el histograma
    plt.savefig(output_path)
    print(f"Histograma guardado en {output_path}")