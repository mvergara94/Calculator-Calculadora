class Calculadora:

    @staticmethod
    def soma(numero_um,numero_dois):
        soma = numero_um + numero_dois
        return soma

    @staticmethod
    def subtracao(numero_um,numero_dois):
        subtracao = numero_um - numero_dois
        return subtracao

    @staticmethod
    def multiplicacao(numero_um,numero_dois):
        multiplicacao = numero_um * numero_dois
        return multiplicacao

    @staticmethod
    def divisao(numero_um,numero_dois):
        divisao = numero_um / numero_dois
        return divisao

    @staticmethod
    def raiz_quadrada(numero):
        raiz = numero**0.5
        print(f'A raiz quadrada de {numero} é : {raiz}')
        return raiz

    @staticmethod
    def elevar_um_numero_a_n(numero,n):
        resultado = numero**n
        print(f'{numero} elevado a {n} é igual a {resultado}')
        return resultado








