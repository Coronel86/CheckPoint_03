import os
import time
import json

from Cliente import Cliente
from Conta import Conta


# Configuração inicial do cliente
cliente = Cliente("Heberton", "123.456.789-00")
conta = Conta("0001", cliente)

# Conta destino para teste de transferência
cliente2 = Cliente("Banco Central", "000.000.000-00")
conta2 = Conta("9999", cliente2)


TEMPO = 3 

def salvar_contas(conta_obj):
    dados = {
        "numero": conta_obj.numero,
        "titular": conta_obj.cliente.nome,
        "cpf": conta_obj.cliente.cpf,
        "saldo": conta_obj.get_saldo()
    }
    #Abre (ou cria) o arquivo 'banco.json' em modo de escrita ("w") com suporte a caracteres especiais (utf-8)
    with open("banco.json", "w", encoding="utf-8") as arquivo: 
        # O 'indent=4' deixa o arquivo visualmente organizado (com recuos de 4 espaços)
        json.dump(dados, arquivo, indent=4)
    print("\nDados salvos com sucesso no banco.json!")

while True:
    
    os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela do terminal conforme o sistema operacional

  
    print(f"Bem-vindo ao Terminal Bank, {cliente.nome}!")
    print("\n#### MENU ####")
    print("\n1- Ver Saldo")
    print("2- Depositar")
    print("3- Sacar")
    print("4- Transferir")
    print("5- Salvar Dados")
    print("6- Sair")

    opcao = input("\nEscolha uma opção: ")

    match opcao:
        case "1":
            print(f"\nSaldo atual: R${conta.get_saldo():.2f}")
            time.sleep(TEMPO)

                    
        case "2":
            valor = float(input("\nDigite o valor para depósito: "))
            conta.depositar(valor)
            time.sleep(TEMPO)
        
        case "3":
            valor = float(input("\nDigite o valor para saque: "))
            conta.sacar(valor)
            time.sleep(TEMPO)

        case "4":
            valor = float(input("Valor da transferência para Conta 9999: "))
            conta.transferir(valor, conta2)
            time.sleep(TEMPO)

        case "5":
            salvar_contas(conta)
            time.sleep(TEMPO)    
                            
        case "6":
            print("\nSaindo... Obrigado por utilizar nosso sistema!")
            time.sleep(TEMPO)
            break
            
        case _:
            print("Opção inválida!")
            time.sleep(TEMPO)