class Item_NF():
    def __init__(self, id,  origem, fornecedor, tipo,  produto, quantidade,valor,  dataEntrada):
        self.id = id
        self.origem = origem
        self.fornecedor = fornecedor
        self.tipo = tipo
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor
        self.dataEntrada = dataEntrada

    def toJson(self):
        return dict(
            id=self.id,
            numero=self.numero,
            fornecedor=self.fornecedor,
            tipo = self.tipo,
            valor = self.valor,
            data_entrada=self.dataEntrada,
            titulo_bancario=self.tituloBancario
        )