def get_ucsc_cyclists(df):
    """
    Filtra y devuelve los ciclistas del club UCSC (Unió Ciclista Sant Cugat).
    """
    return df[df['club_clean'] == 'UCSC']

def best_ucsc_cyclist(df):
    """
    Encuentra el ciclista de UCSC con el mejor tiempo.
    """
    df['time_seconds'] = df['time'].apply(lambda x: sum(int(t) * 60 ** i for i, t in enumerate(reversed(x.split(":")))))
    best_time_row = df[df['club_clean'] == 'UCSC'].sort_values('time_seconds').iloc[0]
    return best_time_row

def cyclist_position_and_percentage(df, cyclist_id):
    """
    Calcula la posición del ciclista en el ranking y su porcentaje respecto al total.
    """
    df = df.sort_values('time').reset_index(drop=True)
    position = df[df['dorsal'] == cyclist_id].index[0] + 1
    total_cyclists = len(df)
    percentage = (1 / total_cyclists) * 100
    return position, percentage