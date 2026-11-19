MAXIMO = 20  # LIMITE = 20 + D (D = 0)


def desconto_valido(percentual):
    if not isinstance(percentual, int):
        return False
    if percentual <= 0:
        return False
    return percentual <= MAXIMO
