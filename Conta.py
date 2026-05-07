from Cliente import Cliente

class Conta:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self._saldo = 0.0

    def get_saldo(self):
        return self._saldo
        
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"\nDepósito de R${valor:.2f} realizado com sucesso.")


    def sacar(self, valor):
        if valor > 0 and valor <= self._saldo:
            self._saldo -= valor
            print(f"\nSaque de R${valor:.2f} realizado com sucesso.")
        else:
            print("\nSaldo insuficiente para realizar o saque.")

    
    def transferir(self, valor, conta_destino):
        if valor > 0 and valor <= self._saldo:
            self._saldo -= valor # Realiza o saque na origem e evitar a mensagem de saque.
            conta_destino._saldo += valor # Realiza o depósito no destino e evitar de aparecer a mensagem deposito.
            print(f"\nTransferência de R${valor:.2f} realizada para conta de destino: {conta_destino.cliente.nome}.")
        else:
            print("\nTransferência cancelada: Saldo insuficiente.")