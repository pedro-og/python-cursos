class Conta:

    # Função construtora
    
    def __init__(self, numero, titular, saldo, limite):
        print(f"Construindo objeto ...{self}")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    # Métodos

    def extrato(self):
        print("O Saldo de {} é {} reais.".format(self.__titular, self.__saldo))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print(f"O valor de {valor} reais passou o limite.")

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite 

    @staticmethod
    def codigo_banco():
        return "001"

        
    @staticmethod
    def codigo_bancos():
        return "{'BB': '001', 'Caixa': '104', 'Bradesco':'237'}"