class Produto():
    def __init__(self, id, descricao, preco, un, codBarras):
        self.id = id
        self.descricao = descricao
        self.preco = preco
        self.un = un
        self.codBarras = codBarras

    def toJson(self):
        return dict(
            id=self.id,
            descricao=self.descricao,
            preco=self.preco,
            un=self.un,
            codigo_barras=self.codBarras
        )