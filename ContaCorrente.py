from Conta import Conta
from Cliente import Cliente

class ContaCorrente(Conta):
    def __init__(self, cliente, taxa):
        super().__init__(cliente)

        self.taxa = taxa
    
    def sacar(self, valor):
        val_taxa = valor + 1.00
        self._saldo -= val_taxa
        print("Saque com taxa Efetuado.")