# ===========================================================
# SISTEMA DO HOTEL - ARQUIVO ÚNICO
# Arrays paralelos obrigatórios (conforme PDF do exercício)
# ===========================================================

# -----------------------------------------------------------
# 1. Função de inicialização (COM OS SEUS DADOS)
# -----------------------------------------------------------
def inicializar_hotel():
    numeros_quartos = [
        101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
        111, 112, 113, 114, 115, 116, 117, 118, 119, 120,
        121, 122, 123, 124, 125, 126, 127, 128, 129, 130,
        131, 132, 133, 134, 135, 136, 137, 138, 139, 140,
        141, 142, 143, 144, 145, 146, 147, 148, 149, 150
    ]

    status_quartos = [
        "livre", "livre", "limpeza", "manutencao", "manutencao", "limpeza", "limpeza", "ocupado", "limpeza", "ocupado",
        "livre", "limpeza", "limpeza", "limpeza", "manutencao", "livre", "livre", "manutencao", "manutencao", "ocupado",
        "manutencao", "ocupado", "manutencao", "limpeza", "ocupado", "ocupado", "manutencao", "livre", "manutencao", "livre",
        "limpeza", "limpeza", "limpeza", "limpeza", "manutencao", "limpeza", "manutencao", "ocupado", "manutencao", "ocupado",
        "ocupado", "manutencao", "ocupado", "limpeza", "ocupado", "limpeza", "manutencao", "manutencao", "ocupado", "ocupado"
    ]

    hospedes_quartos = [
        "", "", "", "", "", "", "", "Maria Eduarda", "", "João Miguel",
        "", "", "", "", "", "", "", "", "", "Ana Clara",
        "", "Pedro Henrique", "", "", "Laura Sofia", "Luiz Otávio", "", "", "", "",
        "", "", "", "", "", "", "", "Isabela Cristina", "", "Carlos Eduardo",
        "Vitória Régia", "", "Hóspede 143", "", "Alice Beatriz", "", "", "", "Vitória Régia", "Jaime Ferreira"
    ]

    dias_estadia = [
        0, 0, 0, 0, 0, 0, 0, 6, 0, 5,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 18,
        0, 3, 0, 0, 9, 4, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 7, 0, 20,
        2, 0, 1, 0, 3, 0, 0, 0, 9, 15
    ]

    return numeros_quartos, status_quartos, hospedes_quartos, dias_estadia


# -----------------------------------------------------------
# 2. Função obrigatória: encontrar índice
# -----------------------------------------------------------
def encontrar_indice_quarto(num_quarto, numeros_quartos):
    for i in range(len(numeros_quartos)):
        if numeros_quartos[i] == num_quarto:
            return i
        
    return -1


# -----------------------------------------------------------
# 3. Operações principais
# -----------------------------------------------------------
def fazer_check_in(num_quarto, nome_hospede, num_dias,
                   numeros_quartos, status_quartos, hospedes_quartos, dias_estadia):

    idx = encontrar_indice_quarto(num_quarto, numeros_quartos)
    if idx == -1 or status_quartos[idx] != "livre":
        return False

    status_quartos[idx] = "ocupado"
    hospedes_quartos[idx] = nome_hospede
    dias_estadia[idx] = num_dias
    return True


def fazer_check_out(num_quarto, numeros_quartos, status_quartos, hospedes_quartos, dias_estadia):
    idx = encontrar_indice_quarto(num_quarto, numeros_quartos)
    if idx == -1 or status_quartos[idx] != "ocupado":
        return None

    nome = hospedes_quartos[idx]

    status_quartos[idx] = "limpeza"
    hospedes_quartos[idx] = ""
    dias_estadia[idx] = 0

    return nome


def marcar_quarto_limpo(num_quarto, numeros_quartos, status_quartos):
    idx = encontrar_indice_quarto(num_quarto, numeros_quartos)
    if idx == -1:
        return False

    if status_quartos[idx] in ("limpeza", "manutencao"):
        status_quartos[idx] = "livre"
        return True

    return False


# -----------------------------------------------------------
# 4. Relatórios e consultas
# -----------------------------------------------------------
def visualizar_ocupacao(numeros_quartos, status_quartos, hospedes_quartos, dias_estadia):
    print("\n======= SITUAÇÃO ATUAL DOS QUARTOS =======\n")
    for i in range(len(numeros_quartos)):
        numero = numeros_quartos[i]
        status = status_quartos[i]

        if status == "ocupado":
            print(f"Quarto {numero} [ocupado] - {hospedes_quartos[i]} ({dias_estadia[i]} dias)")
        else:
            print(f"Quarto {numero} [{status}]")


def encontrar_quartos_por_status(status_busca, numeros_quartos, status_quartos):
    encontrados = []
    for i in range(len(status_quartos)):
        if status_quartos[i] == status_busca:
            encontrados.append(numeros_quartos[i])
    return encontrados


# -----------------------------------------------------------
# 5. Função avançada (opcional)
# -----------------------------------------------------------
def realocar_hospede(quarto_origem, quarto_destino,
                      numeros_quartos, status_quartos, hospedes_quartos, dias_estadia):

    idx_origem = encontrar_indice_quarto(quarto_origem, numeros_quartos)
    idx_destino = encontrar_indice_quarto(quarto_destino, numeros_quartos)

    if idx_origem == -1 or idx_destino == -1:
        return False
    if status_quartos[idx_origem] != "ocupado":
        return False
    if status_quartos[idx_destino] != "livre":
        return False

    hospedes_quartos[idx_destino] = hospedes_quartos[idx_origem]
    dias_estadia[idx_destino] = dias_estadia[idx_origem]
    status_quartos[idx_destino] = "ocupado"

    hospedes_quartos[idx_origem] = ""
    dias_estadia[idx_origem] = 0
    status_quartos[idx_origem] = "limpeza"

    return True


# -----------------------------------------------------------
# 6. MENU INTERATIVO (RODA TUDO NO MESMO ARQUIVO)
# -----------------------------------------------------------
def pausar():
    input("\nPressione ENTER para continuar...")


def menu():
    numeros, status, hospedes, dias = inicializar_hotel()

    while True:
        print("\n" + "=" * 50)
        print("        SISTEMA DE GERENCIAMENTO DO HOTEL")
        print("=" * 50)
        print("1 - Fazer Check-in")
        print("2 - Fazer Check-out")
        print("3 - Listar ocupação dos quartos")
        print("4 - Marcar quarto como limpo")
        print("5 - Buscar quartos por status")
        print("6 - Realocar hóspede (opcional)")
        print("0 - Sair")
        print("=" * 50)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            print("\nEncerrando o sistema...")
            break

        elif opcao == "1":
            try:
                quarto = int(input("Número do quarto: "))
                nome = input("Nome do hóspede: ")
                dias_estadia = int(input("Número de dias: "))

                if fazer_check_in(quarto, nome, dias_estadia, numeros, status, hospedes, dias):
                    print("\n✔ Check-in realizado!")
                else:
                    print("\n❌ Não foi possível realizar o check-in.")
            except:
                print("\n❌ Dados inválidos!")

            pausar()

        elif opcao == "2":
            try:
                quarto = int(input("Número do quarto: "))
                nome = fazer_check_out(quarto, numeros, status, hospedes, dias)

                if nome:
                    print(f"\n✔ Check-out realizado! Hóspede {nome} saiu.")
                else:
                    print("\n❌ Não foi possível realizar o check-out.")
            except:
                print("\n❌ Dados inválidos!")

            pausar()

        elif opcao == "3":
            visualizar_ocupacao(numeros, status, hospedes, dias)
            pausar()

        elif opcao == "4":
            quarto = int(input("Número do quarto: "))
            if marcar_quarto_limpo(quarto, numeros, status):
                print("\n✔ Quarto marcado como limpo!")
            else:
                print("\n❌ Não foi possível marcar como limpo.")
            pausar()

        elif opcao == "5":
            status_busca = input("Status desejado: ").strip().lower()
            quartos = encontrar_quartos_por_status(status_busca, numeros, status)

            if quartos:
                print("\nQuartos encontrados:", quartos)
            else:
                print("\nNenhum quarto com esse status.")

            pausar()

        elif opcao == "6":
            try:
                origem = int(input("Quarto de origem: "))
                destino = int(input("Quarto de destino: "))

                if realocar_hospede(origem, destino, numeros, status, hospedes, dias):
                    print("\n✔ Hóspede realocado!")
                else:
                    print("\n❌ Não foi possível realocar.")
            except:
                print("\n❌ Dados inválidos!")

            pausar()

        else:
            print("\n❌ Opção inválida!")
            pausar()


# -----------------------------------------------------------
# 7. EXECUÇÃO PRINCIPAL
# -----------------------------------------------------------
if __name__ == "__main__":
    menu()