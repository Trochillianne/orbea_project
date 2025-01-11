# Orbea Project 🚴‍♂️

Este proyecto tiene como objetivo analizar datos de una prueba ciclista. A través de varios ejercicios, realizamos tareas como limpieza y anonimización de datos, análisis de tiempos, agrupaciones, y visualizaciones. 

## Ejercicios incluidos

1. **Importación y exploración de datos**:
   - Carga del dataset desde un archivo CSV.
   - Muestra las primeras filas y el número total de ciclistas participantes.

2. **Anonimización y limpieza del dataset**:
   - Anonimización de los nombres de los ciclistas con datos aleatorios.
   - Eliminación de registros de ciclistas que no completaron la prueba.

3. **Agrupamiento de tiempos**:
   - Agrupación de tiempos en franjas de 20 minutos para crear un histograma.
   - Visualización del histograma en la carpeta `img/`.

4. **Limpieza de nombres de clubes**:
   - Normalización de los nombres de clubes para corregir inconsistencias.
   - Cálculo del número de ciclistas por club, ordenados por cantidad de participantes.

5. **Análisis del club UCSC**:
   - Identificación de los ciclistas del club UCSC.
   - Determinación del ciclista más rápido y su posición en el ranking global.

## Requisitos del proyecto

Antes de ejecutar el proyecto, asegúrate de tener instalado lo siguiente:

- Python 3.12 o superior.
- Entorno virtual configurado con las dependencias del archivo `requirements.txt`.

### Instalación

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/Trochillianne/orbea_project.git
   cd orbea_project
   ```

2. Crea y activa un entorno virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

### Ejecución

1. Ejecuta el script principal para realizar todos los análisis:
   ```bash
   python main.py
   ```

2. Los resultados se guardarán en:
   - **Ejercicio 3 (Histograma)**: `img/histograma.png`
   - **Ejercicio 4 (Conteo de clubes)**: `data/club_counts.csv`

### Estructura del proyecto

```plaintext
orbea_project/
|
├── data/
│   ├── dataset.csv         # Dataset original
│   ├── club_counts.csv     # Resultados del análisis de clubes
│
├── img/
│   ├── histograma.png      # Histograma generado
│
├── src/
│   ├── ex1.py              # Ejercicio 1: Importación y exploración
│   ├── ex2.py              # Ejercicio 2: Anonimización y limpieza
│   ├── ex3.py              # Ejercicio 3: Agrupamiento y histograma
│   ├── ex4.py              # Ejercicio 4: Limpieza de clubes
│   ├── ex5.py              # Ejercicio 5: Análisis del UCSC
│
├── main.py                 # Script principal
├── requirements.txt        # Dependencias del proyecto
├── README.md               # Información del proyecto
```

### Contribución

Si deseas colaborar en este proyecto, por favor abre un `pull request` o contacta con el autor principal.
