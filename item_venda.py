class Item_Venda():
    def __init__(self, id,  produto,  quantidade, preco, venda):
        self.id = id
        self.produto = produto
        self.quantidade = quantidade
        self.preco = preco
        self.venda = venda

    def toJson(self):
        return dict(
            id=self.id,
            produto = self.produto,
            quantidade=self.quantidade,
            preco=self.preco,
            venda=self.venda
        )