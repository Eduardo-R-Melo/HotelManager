def inicializar_hotel():
    numeros_quartos = list(range(101, 151))

    status_quartos = ["livre"] * 50

    hospedes_quartos = [""] * 50

    dias_estadia = [0] * 50

    return (numeros_quartos, status_quartos, hospedes_quartos, dias_estadia)

def encontrar_indice_quarto(num_quarto):
    
    for i in range(len(numeros)):
        if numeros[i] == num_quarto:
            return i

    return -1

def fazer_check_in(num_quarto):

    indice = encontrar_indice_quarto(num_quarto)

    if indice == -1:
        print(f'O quarto nº {num_quarto} não existe.')
        return False
    
    elif status[indice] != "livre":
        print(f'Não é possível realizar o check-in.\nStatus: {status[indice]}')
        return False
    
    else:
        nome_hospede = input('Digite o nome do hospede: ')
        num_dias = int(input('Digite quantos dias o cliente ficará hospedado: '))
        
        status[indice] = "ocupado"
        hospedes[indice] = nome_hospede
        dias[indice] = num_dias

        print(f'Check-in feito com sucesso no quarto {num_quarto}')

        return True

def fazer_check_out(num_quarto):
    
    indice = encontrar_indice_quarto(num_quarto)
    
    if indice == -1:
        print('Quarto não existente!')

    else:
        if status[indice] != "ocupado":
            print('O quarto não está ocupado!')

            return None
        
        else:
            temp_nome = hospedes[indice]
            hospedes[indice] = ""
            status[indice] = "limpeza"
            dias[indice] = 0
            print(f'Cliente {temp_nome} saiu')

            return temp_nome

def marcar_quarto_limpo(num_quarto):

    indice = encontrar_indice_quarto(num_quarto)

    if status[indice] != "limpeza" and status[indice] != "manutencao":
        print('Quarto não esta em (Limpeza/Manutenção)')

        return False

    else:
        status[indice] = "livre"
        print('O quarto está disponível novamente')
        return True

def visualizar_ocupacao():
    for i in range(50):
        if status[i] == "ocupado":
            print(f'Quarto: {numeros[i]} - Hóspede: {hospedes[i]} ({dias[i]} dias restantes)')
        else:
            print(f'Quarto: {numeros[i]} [{status[i]}]')

def encontra_quartos_por_status(status_busca):

    quartos_encontrados = []

    for i in range(len(status)):
        if status[i] == status_busca:
            quartos_encontrados.append(numeros[i])
    
    print(f'Quartos encontrados: {quartos_encontrados}')

def realocar_hospede(quarto_origem, quarto_destino):
    indice_origem = encontrar_indice_quarto(quarto_origem)
    indice_destino = encontrar_indice_quarto(quarto_destino)

    if indice_origem == -1 or indice_destino == -1:
        print('\nNão foi possível realocar os hospedes, verifique os quartos novamente!')
    
    elif numeros[indice_origem] == numeros[indice_destino]:
        print('\nOperação inválida')

    elif status[indice_origem] != "ocupado":
        print('\nAVISO: ORIGEM')
        print(f'Quarto de origem: {quarto_origem}, não está ocupado!')

    elif status[indice_destino] != "livre":
        print('\nAVISO: DESTINO')
        print(f'Quarto de destino: {quarto_destino}, está ocupado!')

    else:
        hospedes[indice_destino] = hospedes[indice_origem]
        dias[indice_destino] = dias[indice_origem]
        status[indice_destino] = "ocupado"
        print(f'Hospede: {hospedes[indice_origem]} foi alocado ao quarto: {numeros[indice_destino]}.')

        status[indice_origem] = "limpeza"
        hospedes[indice_origem] = ""
        dias[indice_origem] = 0
        
escolha = 999
numeros, status, hospedes, dias = inicializar_hotel()
print('Bem vindo(a) ao HotelPy!')

while escolha != 0:
    
    print('\nSelecione uma opção: ')
    print('0 - Sair')
    print('1 - Visualizar disponibilidade do quarto')
    print('2 - Realizar check-in')
    print('3 - Realizar check-out')
    print('4 - Concluir limpeza')
    print('5 - Visualizar informações dos quartos')
    print('6 - Busca por status')
    print('7 - Realocar hospede')

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
        
        fazer_check_in(num_quarto)

    if escolha == 3:
        num_quarto = int(input('\nDigite o número do quarto que deseja realizar o check-out: '))

        checkOut = fazer_check_out(num_quarto)

    if escolha == 4:
        num_quarto = int(input('\nQual quarto deseja marcar a limpeza como concluída? '))

        limpeza = marcar_quarto_limpo(num_quarto)

    if escolha == 5:
        consulta = visualizar_ocupacao()

    if escolha == 6:
        status_busca = input('Digite qual status deseja buscar:\nlivre\nocupado\nlimpeza\nmanutencao\n\n')
        
        busca = encontra_quartos_por_status(status_busca)

    if escolha == 7:
        quarto_origem = int(input('\nDigite o número do quarto de origem do hospede: '))
        quarto_destino = int(input('\nDigite o número do quarto de destino do hospede: '))

        realocar = realocar_hospede(quarto_origem, quarto_destino)