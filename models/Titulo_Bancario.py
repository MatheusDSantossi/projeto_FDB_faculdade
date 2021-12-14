class Titulo_Bancario():
    def __init__(self, id, banco, tipo, origem, valor, vencimento, status,  movimento):
        self.id = id
        self.banco = banco
        self.tipo = tipo
        self.origem = origem
        self.valor = valor
        self.vencimento = vencimento
        self.status =status
        self.movimento = movimento

    def toJson(self):
        return dict(
            id=self.id,
            banco = self.banco,
            tipo = self.tipo,
            origem = self.origem,
            valor = self.valor,
            vencimento = self.vencimento,
            status = self.status,
            movimento = self.movimento
        )