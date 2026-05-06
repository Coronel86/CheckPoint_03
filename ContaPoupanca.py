from Conta import Conta
from Cliente import Cliente

class ContaPoupanca(Conta):
    def __init__(self, cliente, juros):
        super().__init__(cliente)

        self.juros = juros

    def render_juros(self):
        return self._saldo * 1.01
    