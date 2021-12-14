class Venda():
    def __init__(self, id, total,  cliente, data):
        self.id = id
        self.total= total
        self.cliente = cliente
        self.data = data

    def toJson(self):
        return dict(
            id=self.id,
            total=self.total,
            cliente=self.cliente,
            data=self.data
        )