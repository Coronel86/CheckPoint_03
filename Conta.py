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
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")


    def sacar(self, valor):
        if valor > 0 and valor <= self._saldo:
            self._saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente para realizar o saque.")

    
    def transferir(self, valor, conta_destino):
        if self.sacar(valor): # Tenta sacar da conta atual
            conta_destino.depositar(valor) # Se der certo, deposita na outra
            print(f"Transferência de R${valor:.2f} realizada para {conta_destino.cliente.nome}.")
            return True
        else:
            print("Transferência cancelada: Saldo insuficiente.")
            return False