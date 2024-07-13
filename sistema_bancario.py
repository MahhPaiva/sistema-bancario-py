menu = """
===== MENU =====
 [1] Depósito
 [2] Saque
 [3] Extrato
 [0] Sair
================
"""
saldo = 0
limite = 500
extrato = ""
LIMITE_SAQUES = 3

valor_deposito = 0

saques_diarios = 3
valor_saque = 0

while True:
    opcao = input((menu))

    if opcao == "1":

        valor_deposito = float(input("Quanto deseja depositar? "))
        if valor_deposito > 0:
            saldo += valor_deposito
            print(f"R${valor_deposito:.2f} depositado na conta")
            extrato = (extrato) + (f"Depósito: R${valor_deposito:.2f}\n")
        else:
            print("Valor inválido, tente novamente!")

    elif opcao == "2":

        if saques_diarios > 0:
            valor_saque = float(input("Quanto deseja sacar? "))

            if valor_saque > 0:

                if (saldo > valor_saque) and (valor_saque <= 500):
                    saldo -= valor_saque
                    print(f"R${valor_saque:.2f} sacado da conta")
                    extrato = (extrato) + (f"Saque:    R${valor_saque:.2f}\n")
                    saques_diarios -= 1
                    
                elif (saldo > valor_saque) and (valor_saque > 500):
                    print("Valor superior ao limite de R$500, tente um valor menor.")

                else:
                    print("Saldo insuficiente.")

            else:
                print("Valor inválido, tente novamente!")

        else:
            print("Já foram realizados os 3 saques diários, tente novamente amanhã!")

    elif opcao == "3":

        print(f"""
======= EXTRATO =======

{extrato}

Saldo atual: R${saldo:.2f}
    
=======================
""")
    
    elif opcao == "0":
        break

    else:
        print("Operação inválida, tente novamente!")