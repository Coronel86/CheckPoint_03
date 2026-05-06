from Conta import Conta
from Cliente import Cliente

class ContaPoupanca(Conta):
    def __init__(self, cliente, juros):
        super().__init__(cliente)

        self.juros = juros

    # Método exclusivo da Poupança e calcula 1% de juros
    
    def render_juros(self):
        rendimento = self._saldo * 1.01
        print(f"Juros aplicados! O saldo rendeu R${rendimento:.2f}.")
    