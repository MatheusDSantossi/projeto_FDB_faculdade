class Nota_Fiscal():
    def __init__(self, id,  numero, fornecedor, tipo,  valor,  dataEntrada, tituloBancario):
        self.id = id
        self.numero = numero
        self.fornecedor = fornecedor
        self.tipo = tipo
        self.valor = valor
        self.dataEntrada = dataEntrada
        self.tituloBancario = tituloBancario

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