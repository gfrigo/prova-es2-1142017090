from cupom import desconto_valido


def test_rf01_percentual_igual_ao_limite_20_e_aceito():
    # Preparar
    percentual = 20

    # Agir
    resultado = desconto_valido(percentual)

    # Verificar
    assert resultado is True


def test_rf02_percentual_21_acima_do_limite_e_rejeitado():
    # Preparar
    percentual = 21

    # Agir
    resultado = desconto_valido(percentual)

    # Verificar
    assert resultado is False


def test_rf03_percentual_zero_e_rejeitado():
    # Preparar
    percentual = 0

    # Agir
    resultado = desconto_valido(percentual)

    # Verificar
    assert resultado is False


def test_rf04_percentual_19_5_nao_inteiro_e_rejeitado():
    # Preparar
    percentual = 19.5

    # Agir
    resultado = desconto_valido(percentual)

    # Verificar
    assert resultado is False
