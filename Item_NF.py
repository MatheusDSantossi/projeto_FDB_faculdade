class Item_NF():
    def __init__(self, id, tipo,  produto, quantidade,valor,  dataEntrada):
        self.id = id
        self.tipo = tipo
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor
        self.dataEntrada = dataEntrada

    def toJson(self):
        return dict(
            id=self.id,
            tipo = self.tipo,
            produto= self.produto,
            quantidade = self.quantidade,
            valor = self.valor,
            data_entrada=self.dataEntrada,
        )