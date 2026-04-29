from main import calcular_desconto, validar_email, formatar_moeda

def test_desconto_comum():
    assert calcular_desconto(100, 10) == 90

def test_desconto_zero():
    assert calcular_desconto(100, 0) == 100

def test_email_valido():
    assert validar_email("contato@empresa.com") is True

def test_email_invalido():
    assert validar_email("usuario_at_gmail.com") is False

def test_formatar_moeda():
    assert formatar_moeda(150.5) == "R$ 150.50"