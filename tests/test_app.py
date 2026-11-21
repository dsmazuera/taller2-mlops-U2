
import unittest

from app import predecir_enfermedad


class TestPrediccionEnfermedades(unittest.TestCase):

    def test_no_enfermo(self):
        resultado = predecir_enfermedad(36, 1, 2)
        self.assertEqual(resultado, "NO ENFERMO")

    def test_enfermedad_leve(self):
        resultado = predecir_enfermedad(38, 4, 3)
        self.assertEqual(resultado, "ENFERMEDAD LEVE")

    def test_enfermedad_aguda(self):
        resultado = predecir_enfermedad(39.5, 8, 5)
        self.assertEqual(resultado, "ENFERMEDAD AGUDA")

    def test_enfermedad_cronica(self):
        resultado = predecir_enfermedad(38, 4, 35)
        self.assertEqual(resultado, "ENFERMEDAD CRÓNICA")

    def test_enfermedad_terminal(self):
        resultado = predecir_enfermedad(40, 9, 15)
        self.assertEqual(resultado, "ENFERMEDAD TERMINAL")


if __name__ == "__main__":
    unittest.main()
