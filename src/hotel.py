
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



