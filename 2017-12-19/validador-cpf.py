import unittest

# Validador de CPF

# Input (onze dígitos inteiros)

# Validar o número digitado - OK
# multiplicar a seq de 9 dígitos (10 - 2) OK
# pegar resto da divisão (*10 / 11) OK
# multiplicar a seq de 10 dígitos (11 - 2) OK
# comparar o validador obtido com o do usuário

# Output (True, False ou None) 


def resto(number1):
    return number1*10 % 11

def valida_numero(numero):
    return type(numero) == int

def valida_qtd_digitos(valor):
    aux = str(valor)
    return len(aux) == 11

def calcula_digito_1(valor):
    aux = list(str(valor)[:-2])
    multiplicador = 10
    soma = 0
    for n in aux:
        soma += multiplicador * int(n)
        multiplicador -= 1
    return soma

def calcula_digito_2(valor):
    aux = list(str(valor))
    multiplicador = 11
    soma = 0

    for n in aux:
        soma += multiplicador * int(n)
        multiplicador -= 1

    return soma

def valida_CPF(cpf):
    if not(valida_numero(cpf) and valida_qtd_digitos(cpf)):
        return False

    digito1 = resto(calcula_digito_1(cpf))

    digito2 = resto(calcula_digito_2(int(str(cpf)[:-2]+str(digito1))))

    return str(cpf)[:-2]+str(digito1)+str(digito2) == str(cpf)


class TestIntelbras(unittest.TestCase):
    def test_resto_100(self):
        self.assertEqual(resto(100),10)

    def test_resto_347(self):
        self.assertEqual(resto(347), 5)

    def test_valida_numero_valido(self):
        self.assertTrue(valida_numero(10))

    def test_valida_numero_invalido(self):
        self.assertFalse(valida_numero('10'))

    def test_valida_digitos_valido(self):
        self.assertTrue(valida_qtd_digitos(99999999999))

    def test_valida_digitos_invalido(self):
        self.assertFalse(valida_qtd_digitos(9999999999))

    def test_cria_primeiro_digito(self):
        self.assertEqual(calcula_digito_1(52998224725), 295)

    def test_cria_segundo_digito(self):
        self.assertEqual(calcula_digito_2(5299822472), 347)

    def test_valida_CPF_valido(self):
        self.assertTrue(valida_CPF(52998224725))

    def test_valida_CPF_invalido(self):
        self.assertFalse(valida_CPF(52998224727))

if __name__ == '__main__':
    unittest.main()