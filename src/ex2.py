from faker import Faker


def name_surname(df):
    """
    Anonimiza la columna 'biker' con nombres y apellidos generados aleatoriamente.
    """
    faker = Faker()
    Faker.seed(42)  # Fijar semilla para resultados reproducibles

    # Generar nombres aleatorios para cada fila
    df['biker'] = df['biker'].apply(lambda _: faker.name())
    return df


def clean_dataset(df):
    """
    Elimina a los ciclistas que no participaron (time == '00:00:00').
    """
    # Filtrar registros donde el tiempo no sea '00:00:00'
    df = df[df['time'] != '00:00:00']
    return df


def get_cyclist_info(df, dorsal):
    """
    Recupera los datos del ciclista con un dorsal específico.
    """
    cyclist_data = df[df['dorsal'] == dorsal]
    return cyclist_data