class Fornecedor():

    def __init__(self, id, razao_social, nome_fantasia, cnpj, inscricao_estadual, logradouro, bairro, municipio, estado, cep,  telefone,  email):
        self.id = id
        self.razao_social = razao_social
        self.nome_fantasia = nome_fantasia
        self.cnpj = cnpj
        self.inscricao_estadual = inscricao_estadual
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
            razao_social = self.razao_social,
            nome_fantasia = self.nome_fantasia,
            cnpj = self.cnpj,
            inscricao_estadual = self.inscricao_estadual,
            logradouro = self.logradouro,
            bairro = self.bairro,
            municipio = self.municipio,
            estado = self.estado,
            cep = self.cep,
            telefone = self.telefone,
            email = self.email
        )