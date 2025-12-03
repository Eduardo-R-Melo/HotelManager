
def inicializar_hotel():
    numero_quartos = list(range(101, 151))

    status_quarto = ["livre"] * 50

    hospedes_quartos = [""] * 50

    dias_estadia = [0] * 50

    return numero_quartos, status_quarto, hospedes_quartos, dias_estadia



def encontrar_indice_quarto(num_quarto, numeros_quartos):

    for i in range(len(numeros_quartos)):
        if numeros_quartos[i] == num_quarto:
            return i

    return -1



def fazer_check_in(num_quarto, nome_hospede, num_dias, numeros_quartos, status_quartos, hospedes_quartos, dias_estadia):

    i = encontrar_indice_quarto(num_quarto, numeros_quartos)

    if i == -1:
        return False

    if status_quartos[i] != "livre":
        return False

    status_quartos[i] = "ocupado"
    hospedes_quartos[i] = nome_hospede
    dias_estadia[i] = num_dias

    return True



def fazer_check_out(num_quarto, numeros_quartos, status_quartos, hospedes_quartos, dias_estadia):

    i = encontrar_indice_quarto(num_quarto, numeros_quartos)

    if i == -1:
        return None
    
    if status_quartos[i] != "ocupado":
        return None

    nome_hospede = hospedes_quartos[i]
    status_quartos[i] = "limpeza"
    hospedes_quartos[i] = ""
    dias_estadia = 0

    return nome_hospede



escolha = 999
numeros, status, hospedes, dias = inicializar_hotel()
print('Bem vindo(a) ao Hotel!')



while escolha != 0:

    print('\nSelecione uma opção:')
    print('0 - Sair')
    print('1 - Visualizar disponibilidade de Quarto')
    print('2 - Realizar check-in do Quarto')
    print('3 - Realizar check-out do Quarto')
    escolha = int(input('\nO que deseja visualizar? '))


    if escolha == 1:
        n = int(input('\nDigite o número do quarto que deseja visualizar: '))

        indice = encontrar_indice_quarto(n, numeros)

        if indice == -1:
            print("Quarto não encontrado.")
        else:
            print("Quarto:", numeros[indice])
            print("Status:", status[indice])
            print("Hóspede:", hospedes[indice])
            print("Dias de estadia:", dias[indice])



    elif escolha == 2:
        num_quarto = int(input("\nDigite o número do quarto para check-in: "))
        nome_hospede = input("Nome do hóspede: ")
        num_dias = int(input("Quantidade de dias de estadia: "))

        resultado = fazer_check_in(
            num_quarto,
            nome_hospede,
            num_dias,
            numeros,
            status,
            hospedes,
            dias
        )

        if resultado:
            print(f"\nCheck-in feito com sucesso no quarto {num_quarto}!")
        else:
            print(f"\nNão foi possível realizar o check-in no quarto {num_quarto}.")
    


    elif escolha == 3:
        num_quarto = int(input("\nDigite o número do quarto para check-out: "))

        nome = fazer_check_out(
            num_quarto,
            numeros,
            status,
            hospedes,
            num_dias
        )

        if nome is None:
            print(f"\nNão foi possível fazer check-out do quarto {num_quarto}.")

        else:
            print(f"\nCheck-out realizado com sucesso!")
            print(f"Hóspede que saiu: {nome}")
            print(f"Quarto {num_quarto} agora está com status: {status[ encontrar_indice_quarto(num_quarto, numeros) ]}")

