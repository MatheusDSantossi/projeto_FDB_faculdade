class Saldo_Estoque():
    def __init__(self, id, descricao, estoque, saldo):
        self.id = id
        self.descricao = descricao
        self.estoque = estoque
        self.saldo = saldo

    def toJson(self):
        return dict(
            id=self.id,
            descricao=self.descricao,
            estoque=self.estoque,
            saldo=self.saldo
        )