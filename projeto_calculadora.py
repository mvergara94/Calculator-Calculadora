class CalculadoraSimples:

    @staticmethod
    def soma_de_dois_numeros(numero_um,numero_dois):
        soma = numero_um + numero_dois
        print(f'A soma de {numero_um} + {numero_dois} é {soma}')
        return soma

    @staticmethod
    def subtracao_de_dois_numeros(numero_um,numero_dois):
        subtracao = numero_um - numero_dois
        print(f'A subtração de {numero_um} - {numero_dois} é {subtracao}')
        return subtracao

    @staticmethod
    def multiplicacao_de_dois_numeros(numero_um,numero_dois):
        multiplicacao = numero_um * numero_dois
        print(f'A multiplicação de {numero_um} x {numero_dois} é {multiplicacao}')
        return multiplicacao

    @staticmethod
    def divisao_de_dois_numeros(numero_um,numero_dois):
        divisao = numero_um * numero_dois
        print(f'A divisão de {numero_um} por {numero_dois} é {divisao}')
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

class CalculadoraDeListas:

    def __init__(self, conjunto):
        if ValidacaoLista.validacao(conjunto):
            self.conjunto = conjunto
        else:
            raise ValueError('Conjunto de dados possui argumento nao numérico')

    def soma_do_conjunto(self):
        soma_do_conjunto = sum(self.conjunto)
        print(f'A soma do Conjunto é {soma_do_conjunto}')
        return soma_do_conjunto

    def media_do_conjunto(self):
        media = self.soma_do_conjunto()/len(self.conjunto)
        print(f'A média do conjunto é {media}')
        return media

class ValidacaoLista:

    @staticmethod
    def validacao(conjunto):
        for item in conjunto:
            if type(item) == str:
                return False
        return True







