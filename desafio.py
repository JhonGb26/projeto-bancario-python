#Variaveis:

saldo = 0
limite = 500
saque = 0
extrato = ""
limite_saque = 3

#Menu:

menu = "=" * 10 + " MENU " + "=" * 10
menu += "\n"
menu += "1 - Depositar\n"
menu += "2 - Sacar\n"
menu += "3 - Extrato\n"
menu += "4 - Sair\n"
menu += "=" * 22
menu += "\n"




while True:

    opcao = int(input(menu + "Digite a opção desejada: "))

    if opcao == 1:
        valor = float(input('Informe o quanto quer depositar? '))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: {valor:.2f}\n"
            

        else:
            print("Sua operação falhou! Confira o valor e tente novamente.")

    elif opcao == 2:
        valor = float(input('Informe o quanto quer sacar? '))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saque = saque >= limite_saque

        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque é maior que o limite.")

        elif excedeu_saque:
            print("Operação falhou! Número máximo de saque.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: {valor:.2f}\n"
            saque += 1
            
    
        else:
            print("Sua operação falhou! Confira o valor e tente novamente.")
    
    elif opcao == 3:
        
        Extrato = "=" * 10 + " Extrato " + "=" * 10
        Extrato += "\n"
        Extrato += "Não foram realizadas operações\n" if not extrato else extrato
        Extrato += f"Saldo: {saldo:.2f}\n"
        Extrato += "=" * 22
        Extrato += "\n"
        print(Extrato)
    
    elif opcao == 4:
        print("Sair")
        break

    else:
        print("Opção inválida, por favor tente novamente.")



