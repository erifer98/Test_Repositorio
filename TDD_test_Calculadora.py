import unittest
from Calculadora import calculadora

class TestCal(unittest.TestCase):

    def test_debe_iniciar_con_uno(self):
        calc = calculadora()
        self.assertEqual(0,calc.valor())

if __name__=='__main__':
    unittest.main()