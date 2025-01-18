# Orbea Project

Este proyecto analiza datos de una prueba ciclistica, proporcionando información sobre los participantes, tiempos y clubes ciclistas.
Además, se implementan procesos para limpiar y estructurar datos, generar estadísticas y visualizar datos. 

## **Estructura del Proyecto**
- **`src/`**: Contiene los scripts principales (`ex1.py`, `ex2.py`, ..., `ex5.py`).
- **`main.py`**: Script principal para ejecutar los ejercicios.
- **`tests/`**: Pruebas unitarias para validar las funcionalidades.
- **`data/`**: Archivos de datos utilizados en el proyecto (`dataset.csv`como dataset original y `club_counts.csv`como resultado del análisis de clubes).
- **`img/`**: Imágenes generadas como parte de los resultados (por ejemplo, histogramas).
- **`requirements.txt`**: Librerías necesarias para ejecutar el proyecto.
- **`LICENSE`**: Licencia del proyecto.

## Descripción de los ejercicios

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

### Instrucciones de instalación

1. Clona este repositorio desde GitHub:
   ```bash
   git clone https://github.com/Trochillianne/orbea_project.git
   cd orbea_project
   ```

2. Crea y activa un entorno virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate     # En Windows: venv\Scripts\activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
   
3. Instala setup:
   ```bash
   python setup.py install
   ```

### Ejecución

1. Para ejecutar todos los ejercicios, ejecuta el script principal:
   ```bash
   python main.py
   ```

2. Cada ejercicio generará salidas específicas en la terminal y, los archivos de datos o imágenes en las siguientes carpetas: 
   - **Ejercicio 3 (Histograma)**: `img/histograma.png`
   - **Ejercicio 4 (Conteo de clubes)**: `data/club_counts.csv`

## Tests

Para ejecutar las pruebas unitarias, ejecútalo desde la raíz del proyecto

```bash
python -m unittest discover -s tests
```

Esto ejecutará todas las pruebas en el directorio `tests/` y mostrará un informe en la terminal.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.
