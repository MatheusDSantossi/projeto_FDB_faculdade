class Estoque():
    def __init__(self, id, descricao):
        self.id = id
        self.descricao = descricao

    def toJson(self):
        return dict(
            id=self.id,
            descricao=self.descricao,
        )