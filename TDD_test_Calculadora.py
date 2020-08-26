import unittest

from Calculadora import Calculadora

class Test_1 (unittest.TestCase):
    
    def Calculadora_debe_iniciar_en_cero(self):
        calc=Calculadora()
        self.assertEqual(0,calc.valor())

