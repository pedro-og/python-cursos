# def cria_conta(numero, titular, saldo, limite):
#     conta = {"numero": numero, "titular": titular, "saldo":saldo, "limite": limite}
#     return conta

# def deposita(conta, valor):
#     conta["saldo"] += valor

# def saca(conta, valor):
#     conta["saldo"] -= valor

# def extrato(conta):
#     print(f"Saldo é {conta['saldo']}")

class Retangulo:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__area = x * y

    def obter_area(self):
        return self.__area

        