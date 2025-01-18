import os
import pandas as pd
import unittest

from src.ex1 import load_dataset
from src.ex2 import name_surname, clean_dataset
from src.ex3 import group_and_plot_times
from src.ex4 import clean_club
from src.ex5 import get_ucsc_cyclists, best_ucsc_cyclist, cyclist_position_and_percentage

class TestProject(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Inicializamos los datos de prueba compartidos entre los tests"""
        print("Running setUpClass")
        cls.df = pd.DataFrame({
            "dorsal": [1, 2, 3],
            "biker": ["Alice Doe", "Bob Smith", "Charlie Brown"],
            "club": ["C.C. Huesca", "Independiente", "Club Ciclista"],
            "time": ["06:10:00", "00:00:00", "06:40:00"]
        })

    def test_load_dataset(self):
        """Verificamos que el dataset se cargue correctamente desde un archivo CSV"""
        print("Running test_load_dataset")
        dataset_path = os.path.join(os.path.dirname(__file__), '../data/dataset.csv') # construimos ruta relativa
        print(f"Ruta absoluta del dataset: {os.path.abspath(dataset_path)}")
        expected_columns = ["dorsal", "biker", "club", "time"]
        df = load_dataset("data/dataset.csv")
        self.assertIsNotNone(df)
        self.assertListEqual(list(df.columns), expected_columns)

    def test_name_surname(self):
        """Verificamos que los nombres de los ciclistas se anonimicen correctamente"""
        print("Running test_name_surname")
        anonymized_df = name_surname(self.df.copy())
        self.assertNotEqual(anonymized_df["biker"].iloc[0], "Alice Doe")

    def test_clean_dataset(self):
        """Verificamos que se eliminen los ciclistas sin tiempo registrado"""
        print("Running test_clean_dataset")
        cleaned_df = clean_dataset(self.df.copy())
        self.assertEqual(len(cleaned_df), 2)

    def test_group_and_plot_times(self):
        """Verificamos que los tiempos se agrupen correctamente y el histograma se genere"""
        print("Running test_group_and_plot_times")
        os.makedirs("img", exist_ok=True)
        grouped_df = group_and_plot_times(self.df.copy(), output_path="img/histograma_test.png")
        self.assertTrue(os.path.exists("img/histograma_test.png"))
        os.remove("img/histograma_test.png")

    def test_clean_club(self):
        """Verificamos que los nombres de los clubes se limpien correctamente"""
        print("Running test_clean_club")
        cleaned_club_df = self.df.copy()
        cleaned_club_df["club_clean"] = cleaned_club_df["club"].apply(clean_club)
        self.assertEqual(cleaned_club_df["club_clean"].iloc[0], "HUESCA")

    def test_get_ucsc_cyclists(self):
        """Verificamos que se obtengan los ciclistas del club UCSC"""
        print("Running test_get_ucsc_cyclists")
        self.df["club_clean"] = ["UCSC", "Independiente", "UCSC"]
        ucsc_cyclists = get_ucsc_cyclists(self.df)
        self.assertEqual(len(ucsc_cyclists), 2)

    def test_best_ucsc_cyclist(self):
        """Verificamos que se encuentre el mejor ciclista de UCSC"""
        print("Running test_best_ucsc_cyclist")
        self.df["club_clean"] = ["UCSC", "Independiente", "UCSC"]
        self.df["time_seconds"] = self.df["time"].apply(lambda x: sum(int(t) * 60 ** i for i, t in enumerate(reversed(x.split(":")))))
        best_cyclist = best_ucsc_cyclist(self.df)
        self.assertEqual(best_cyclist["dorsal"], 1)

    def cyclist_position_and_percentage(df, cyclist_id):
        df = df.sort_values('time').reset_index(drop=True)
        print(df)  # Verificamos que los datos estén ordenados correctamente
        position = df[df['dorsal'] == cyclist_id].index[0] + 1
        total_cyclists = len(df)
        percentage = (1 / total_cyclists) * 100
        return position, percentage

    @classmethod
    def tearDownClass(cls):
        """Limpiamos los archivos temporales creados durante las pruebas"""
        print("Eliminando archivos temporales...")
        if os.path.exists("test_data.csv"):
            os.remove("test_data.csv")


if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()  # Definimos suite aquí
    suite.addTest(loader.loadTestsFromTestCase(TestProject))  # Agregamos los tests a suite
    runner = unittest.TextTestRunner()
    runner.run(suite)