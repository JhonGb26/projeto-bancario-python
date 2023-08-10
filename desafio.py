import textwrap

def menu():

    menu = "=" * 10 + " MENU " + "=" * 10
    menu += "\n"
    menu += "1 - Depositar\n"
    menu += "2 - Sacar\n"
    menu += "3 - Extrato\n"
    menu += "4 - Novo usuário\n"
    menu += "5 - Nova conta\n"
    menu += "6 - Listar conta\n"
    menu += "7 - Sair\n"
    menu += "=" * 22
    menu += "\n"
    return int(input(textwrap.dedent(menu + "Digite a opção desejada: ")))

def depositar(saldo, valor, extrato, /):
      
    if valor > 0:
        saldo += valor
        extrato += f"Deposito:\tR$ {valor:.2f}\n"
        print(f'Seu novo saldo é: {saldo}')

    else:
        print("Sua operação falhou! Confira o valor e tente novamente.")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saque, limite_saque):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = numero_saque >= limite_saque

    if excedeu_saldo:
      print("Operação falhou! Saldo insuficiente.")

    elif excedeu_limite:
     print("Operação falhou! O valor do saque é maior que o limite.")

    elif excedeu_saque:
      print("Operação falhou! Número máximo de saque.")

    elif valor > 0:
      saldo -= valor
      extrato += f"Saque:\t\tR$ {valor:.2f}\n"
      numero_saque += 1
      print("Saque Realizado com Sucesso! ")

    else:
        print("Sua operação falhou! Confira o valor e tente novamente.")

    return saldo, extrato

def exibir_extrato(saldo, /,*, extrato):
   Extrato = "=" * 10 + " Extrato " + "=" * 10
   Extrato += "\n"
   Extrato += "Não foram realizadas operações\n" if not extrato else extrato
   Extrato += f"Saldo: {saldo:.2f}\n"
   Extrato += "=" * 22
   Extrato += "\n"
   print(Extrato)

def criar_usuario(usuarios):
   cpf = input("Informe o CPF (Somente números): ")
   usuario = filtrar_usuario(cpf, usuarios)

   if usuario:
      print("Já existe usuário com esse CPF! ")
      return
   nome = input("Informe o nome completo: ")
   data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
   endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

   usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

   print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
   usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
   return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
  cpf = input("Informe o CPF do usuário: ")
  usuario = filtrar_usuario(cpf, usuarios)

  if usuario:
     print("Conta criada com sucesso!")
     return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
  
  print("Usuário não encontrado, fluxo de criação de conta encerrada")

def listar_contas(contas):
    for conta in contas:
       linha = f"""\
        Agência:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
       """
       print("=" * 100)
       print(textwrap.dedent(linha))

def main():

    limite_saque = 3
    agencia = "001"

    saldo = 0
    limite = 500
    numero_saque = 0
    extrato = ""
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == 1:
            valor = float(input("Informe o valor do depósito: ")) 

            saldo, extrato = depositar(saldo, valor, extrato)        

        elif opcao == 2:
            valor = float(input("Informe o quanto quer sacar? "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saque=numero_saque,
                limite_saque=limite_saque,
            )
            
        
        elif opcao == 3:
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 4:
            criar_usuario(usuarios)

        elif opcao == 5:
            numero_conta = len(contas) + 1
            conta = criar_conta(agencia, numero_conta, usuarios)
            if conta:
               contas.append(conta)
        
        elif opcao == 6:
           listar_contas(contas)
             
        elif opcao == 7:
            print("Sair")
            break

        else:
            print("Opção inválida, por favor tente novamente.")

main()
