from unittest import TestCase
from Cuenta import Cuenta


class TestCuenta(TestCase):

    def test_depositar(self):
        c = Cuenta
        self.assertEqual(c.depositar(c, 5), 5)



class TestCuenta(TestCase):
    def test_retiro(self):
        c = Cuenta
        c.setSaldo(c,20)
        self.assertEqual(c.retiro(c, 10), 10)
