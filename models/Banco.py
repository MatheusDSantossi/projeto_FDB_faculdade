class Banco():

    def __init__(self, id, codigo_bancario, nome, agencia, conta, logradouro, bairro, municipio, estado, cep,  telefone,  email, saldo):
        self.id = id
        self.codigo_bancario = codigo_bancario
        self.nome = nome
        self.agencia = agencia
        self.conta = conta
        self.logradouro = logradouro
        self.bairro = bairro
        self.municipio = municipio
        self.estado = estado
        self.cep = cep
        self.telefone = telefone
        self.email = email
        self.saldo = saldo

    def toJson(self):
        return dict(
            id=self.id,
            codigo_bancario=self.codigo_bancario,
            nome=self.nome,
            agencia=self.agencia,
            conta=self.conta,
            logradouro = self.logradouro,
            bairro = self.bairro,
            municipio = self.municipio,
            estado = self.estado,
            cep = self.cep,
            telefone = self.telefone,
            email = self.email,
            saldo = self.saldo
        )