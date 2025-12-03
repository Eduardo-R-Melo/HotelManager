def inicializar_hotel():
    numero_quartos = list(range(101, 151))

    status_quarto = ["livre"] * 50

    hospedes_quartos = [""] * 50

    dias_estadia = [0] * 50

    return numero_quartos, status_quarto, hospedes_quartos, dias_estadia

def encontrar_indice_quarto(num_quarto):
    
    for i in range(len(numeros)):
        if numeros[i] == num_quarto:
            return i

    return -1

def fazer_check_in(num_quarto, nome_hospede, num_dias):

    i = encontrar_indice_quarto(num_quarto)

    if i == -1:
        return False
    
    if status[i] != "livre":
        return False
    
    status[i] = "ocupado"
    hospedes[i] = nome_hospede
    dias[i] = num_dias

    return True

def fazer_check_out(num_quarto):
    
    indice = encontrar_indice_quarto(num_quarto)

    if status[indice] != "ocupado":
        print('O quarto não está ocupado!')

        return None
    
    else:
        temp_nome = hospedes[indice]
        hospedes[indice] = ""
        status[indice] = "limpeza"
        dias[indice] = 0
        print(f'O cliente {temp_nome} saiu')

        return temp_nome
    
escolha = 999
numeros, status, hospedes, dias = inicializar_hotel()
print('Bem vindo(a) ao HotelPy!')

def mostrar_listas():
    print(numeros, status, hospedes, dias)

while escolha != 0:
    
    print('\nSelecione uma opção: ')
    print('0 - Sair')
    print('1 - Visualizar disponibilidade do quarto')
    print('2 - Realizar check-in')
    print('3 - Realizar check-out')

    escolha = int(input('\nO que deseja visualizar? '))

    if escolha == 0:
        print('Encerrando a aplicação...')

    if escolha == 1:
        num_quarto = int(input('\nDigite o número do quarto que deseja visualizar: '))

        indice = encontrar_indice_quarto(num_quarto)

        if indice == -1:
            print('Quarto não encontrado.')
        
        else:
            print(f'Quarto: {numeros[indice]}')
            print(f'Status: {status[indice]}')
            print(f'Hóspede: {hospedes[indice]}')
            print(f'Dias de estadia: {dias[indice]}')

    if escolha == 2:
        num_quarto = int(input('\nDigite o número do quarto que deseja realizar o check-in: '))
        
        indice = encontrar_indice_quarto(num_quarto)

        if status[indice] != "livre":
            print(f'Não é possível realizar o check-in.\nStatus: {status[indice]}')

        else:
            nome_hospede = input('Digite o nome do hospede: ')
            num_dias = int(input('Digite quantos dias o cliente ficará hospedado: '))

            resultado = fazer_check_in(
                num_quarto,
                nome_hospede,
                num_dias
            )

            if resultado:
                print(f'Check-in feito com sucesso no quarto {num_quarto}')
            
            else:
                print(f'Não foi possível realizar o check-in no quarto {num_quarto}')

    if escolha == 3:
        
        num_quarto = int(input('\nDigite o número do quarto que deseja realizar o check-out: '))

        checkOut = fazer_check_out(num_quarto)