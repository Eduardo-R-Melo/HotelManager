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


# Verifica se encontra o quarto utilizando os indices
numeros, status, hospedes, dias = inicializar_hotel()
n = int(input('Digite o número do quarto que deseja visualizar: '))

indice = encontrar_indice_quarto(n, numeros)

if indice == -1:
    print("Quarto não encontrado.")
else:
    print("Quarto:", numeros[indice])
    print("Status:", status[indice])
    print("Hóspede:", hospedes[indice])
    print("Dias de estadia:", dias[indice])


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

