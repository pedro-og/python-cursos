class Data:

    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada(self):
        print('{:02d}/{:02d}/{}'.format(self.dia, self.mes, self.ano))

data_obj = Data(2, 3, 2022)
data_obj.formatada()
