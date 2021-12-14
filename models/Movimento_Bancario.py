class Movimento_Bancario():
    def __init__(self, id, banco, tipo, origem, valor, dataMovimento):
        self.id = id
        self.banco = banco
        self.tipo = tipo
        self.origem = origem
        self.valor = valor
        self.dataMovimento = dataMovimento

    def toJson(self):
        return dict(
            id=self.id,
            banco = self.banco,
            tipo = self.tipo,
            origem = self.origem,
            valor = self.valor,
            data_movimento = self.dataMovimento
        )