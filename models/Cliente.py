class Cliente():

    def __init__(self, id, nome, cpf, logradouro, bairro, municipio, estado,
                 cep, telefone, email):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.logradouro = logradouro
        self.bairro = bairro
        self.municipio = municipio
        self.estado = estado
        self.cep = cep
        self.telefone = telefone
        self.email = email

    def toJson(self):
        return dict(
            id=self.id,
            nome=self.nome,
            cpf=self.cpf,
            logradouro=self.logradouro,
            bairro=self.bairro,
            municipio=self.municipio,
            estado=self.estado,
            cep=self.cep,
            telefone=self.telefone,
            email=self.email
        )