menu = """
O que deseja?
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

menu_secundario = """
Deseja realizar mais alguma operação?

[y]Sim
[q]Não

=> """
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

print("Bom dia, bem vindo ao nosso auto-atendimento.")
opcao = input(menu)

while True:    

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("\nDepósito efetuado com sucesso.")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("\nRetire o dinheiro.")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "y":
        opcao = input(menu)
        continue

    elif opcao == "q":
        print("\nAgradecemos sua visita, tenha um bom dia!")
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

    opcao = input(menu_secundario)