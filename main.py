import os
import time
from Cliente import Cliente
from Conta import Conta

cliente = Cliente("Heberton", "123.456.789-00")
conta = Conta("0001", cliente)

TEMPO = 3 



while True:
    
    os.system('cls' if os.name == 'nt' else 'clear')

  
    print("\n#### MENU ####")
    print("\n1- Ver Saldo")
    print("2- Depositar")
    print("3- Sacar")
    print("4- Sair") 
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
            print("\nSaindo... Obrigado por utilizar nosso sistema!")
            time.sleep(TEMPO)
            break
            
        case _:
            print("Opção inválida!")
            time.sleep(TEMPO)