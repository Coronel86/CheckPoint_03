from Conta import Conta
from Cliente import Cliente

class ContaCorrente(Conta):
    def __init__(self, cliente, taxa):
        super().__init__(cliente)

        self.taxa = taxa
    
    # Polimorfismo: alterando o comportamento do saque para incluir a taxa
    
    def sacar(self, valor):   
        val_taxa = valor + 1.00
        if val_taxa <= self._saldo:
            self._saldo -= val_taxa
            print(f"Saque de R${valor:.2f} (Taxa: R$1.00) realizado com sucesso.")
        else:
            print("Saldo insuficiente para cobrir o saque e a taxa.")