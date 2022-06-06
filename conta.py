

class Conta:

    # Função construtora
    
    def __init__(self, numero, titular, saldo, limite):
        print(f"Construindo objeto ...{self}")
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    # Métodos

    def extrato(self):
        print("O Saldo de {} é {} reais.".format(self.titular, self.saldo))

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor
