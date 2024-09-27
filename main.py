APP_NAME = " SysBank ".center(30, "-")
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def print_quit_message():
    print("Obrigado por usar nossos serviços! Até breve")

print("\n\n\n" + APP_NAME)
print(" Seja bem vindo!")

while True:

    print("Entre com a operação:")
    opcao = input(menu).lower()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"\n Valor {valor} depositado com sucesso!")
            print(f" Agora seu saldo é: {saldo}")

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

            print(f"\n Saque de {valor} realizado com sucesso!")
            print(f" Agora seu saldo é: {saldo}")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        print_quit_message()
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

    resposta = input("\nAperte Enter para Continuar ou [q] para sair ")
    if(resposta.lower() == "q"):
        print_quit_message()
        break

print(APP_NAME)
