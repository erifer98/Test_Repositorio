import unittest
from Calculadora import calculadora

class TestCal(unittest.TestCase):

       def test_debe_iniciar_con_uno(self):
        calc = calculadora()
        self.assertEqual(0,calc.valor())
    
    def test_suma_2_mas_3_es_cinco(self):
        calc= calculadora()
        calc.suma(2,3)
        self.assertEqual(5,calc.valor())

if __name__=='__main__':
    unittest.main()
