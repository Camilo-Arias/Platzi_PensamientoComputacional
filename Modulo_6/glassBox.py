import unittest

def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False

class glassBoxTest(unittest.TestCase):
    #test1
    def test_es_mayor_edad(self):
        edad = 20

        result = es_mayor_de_edad(edad)

        self.assertEqual(result, True)

    #test2
    def test_es_menor_edad(self):
        edad = 15

        result = es_mayor_de_edad(edad)

        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main(verbosity=2)
