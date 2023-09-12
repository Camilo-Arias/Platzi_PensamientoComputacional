import unittest

#Defined function what we go to testing
def suma(num_1, num_2):
    return num_1+num_2

class BlackBoxTest(unittest.TestCase):
    #test1
    def test_suma_dos_positivos(self):
        num_1 = 10
        num_2 = 5

        result = suma(num_1, num_2)

        self.assertEqual(result, 15)
    #test2
    def test_suma_dos_negativos(self):
        num_1 = -10
        num_2 = -7

        result = suma(num_1, num_2)
        self.assertEqual(result, -17)

if __name__ == '__main__':
    unittest.main(verbosity=2)