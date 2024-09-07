import sys
import os
import unittest

# Add the 'src' directory to the Python path so 'calculadora' can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


class TestCalcular(unittest.TestCase):
    # TODO Adiciona tus pruebas unitarias aquí.
    # Ejemplo:   
    # def test_suma(self):
    #     valor_esperado = 3
    #     valor_actual = calcular(1, 2, '+')
    #     self.assertEqual(valor_esperado, valor_actual)
    import unittest

from cuenta_bancaria import CuentaBancaria

class TestCuentaBancaria(unittest.TestCase):
    def setUp(self):
        self.cuenta = CuentaBancaria("Juan Pérez", "123456789", 1000.0)

    def test_ingresar(self):
        # Prueba  ingresar
        self.cuenta.ingresar(500)
        valor_esperado = 1500.0
        valor_actual = self.cuenta.get_saldo()
        self.assertEqual(valor_esperado, valor_actual)  # Verifica si el saldo es correcto

    def test_retirar(self):
        # Prueba retirar
        self.cuenta.retirar(200)
        valor_esperado = 800.0
        valor_actual = self.cuenta.get_saldo()
        self.assertEqual(valor_esperado, valor_actual)  # ver si el saldo es correcto
        self.cuenta.retirar(1000)  # Intentar retirar de mas
        # El saldo no debería cambiar después de intentar retirar más de lo disponible
        self.assertEqual(self.cuenta.get_saldo(), 800.0)

if __name__ == "__main__":
    unittest.main()