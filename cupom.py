MAXIMO = 20  # LIMITE = 20 + D (D = 0)


def desconto_valido(percentual):
    if percentual <= 0:
        return False
    return percentual <= MAXIMO
