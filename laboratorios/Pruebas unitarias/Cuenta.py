class Cuenta:

    nombre = ""
    numero = 0
    saldo = 0.00

    def __init__(self, nombre, numero, saldo):
        self.nombre = nombre
        self.numero = numero
        self.saldo = saldo

    def getSaldo(self):
        return self.saldo

    def setSaldo(self,saldo):
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo = self.saldo + monto
        return self.saldo

    def retiro(self, monto):
        self.saldo = self.saldo - monto
        return self.saldo