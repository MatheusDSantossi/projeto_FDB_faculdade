import json

from flask import Flask, request, render_template
from models.User import User
from util_db import conexao_db
from templates.formularios import FormularioLogin



app = Flask(__name__)
app.config.from_object('config')

@app.route('/', methods=['GET', 'POST'])
def mainPage():
        return "O sistema é só backend meu patrão,  infelizmente, vai dar trabalho pra corrigir =/ mas corrija com amor,  que a gente fez com amor, e  com amor  a  nota é 10"

@app.route('/produtos/')
def getProdutos():
    produtos = conexao_db.get_all_Produtos()
    produtos = [Produto.toJson() for Produto in produtos]
    return json.dumps(produtos)

@app.route('/produtos/add/', methods=['POST'])
def new_produto():
    if request.method == 'POST':
        descricao = request.form.get('descricao')
        preco = request.form.get('preco')
        unidade_medida = request.form.get('unidade_medida')
        codigo_barras = request.form.get('codigo_barras')
        conexao_db.novo_Produto(descricao,preco,unidade_medida,codigo_barras)


@app.route('/produtos/<int:id>/', methods=['GET', 'POST'])
def getProduto(id):

    if request.method == 'GET':
        return conexao_db.get_produto_by_id(id).toJson()
    if request.method == 'POST':
        pass
        #return render_template('Alterar_Produto.html', descricao=produto.descricao, codigo_barras = produto.codBarras, unidade_medida=produto.un, preco = produto.preco)


@app.route('/fornecedores/')
def getFornecedor():
    fornecedores = conexao_db.get_all_Fornecedores()
    fornecedores = [Fornecedor.toJson() for Fornecedor in fornecedores]
    return json.dumps(fornecedores)

@app.route('/fornecedores/add/', methods=['POST'])
def new_fornecedor():

    if request.method == 'POST':
        razao_social = request.form.get('razao_social')
        nome_fantasia = request.form.get('nome_fantasia')
        cnpj = request.form.get('cnpj')
        inscricao_estadual = request.form.get('inscricao_estadual')
        logradouro = request.form.get('logradouro')
        bairro = request.form.get('bairro')
        municipio = request.form.get('municipio')
        estado = request.form.get('estado')
        cep = request.form.get('cep')
        telefone = request.form.get('telefone')
        email = request.form.get('email')

        conexao_db.novo_Fornecedor(razao_social, nome_fantasia, cnpj, inscricao_estadual, logradouro, bairro, municipio, estado, cep, telefone, email)


@app.route('/fornecedores/<int:id>/', methods=['GET', 'POST'])
def getFornecedor(id):

    if request.method == 'GET':
        return conexao_db.get_fornecedor_by_id(id).toJson()
    if request.method == 'POST':
        pass
        #return render_template('Alterar_Produto.html', descricao=produto.descricao, codigo_barras = produto.codBarras, unidade_medida=produto.un, preco = produto.preco)

@app.route('/clientes/')
def getCliente():
    clientes = conexao_db.get_all_Clientes()
    clientes = [Cliente.toJson() for Cliente in clientes]
    return json.dumps(clientes)


@app.route('/clientes/add/', methods=['POST'])
def new_cliente():
    if request.method == 'POST':
        nome = request.form.get('nome')
        cpf = request.form.get('cpf')
        logradouro = request.form.get('logradouro')
        bairro = request.form.get('bairro')
        municipio = request.form.get('municipio')
        estado = request.form.get('estado')
        cep = request.form.get('cep')
        telefone = request.form.get('telefone')
        email = request.form.get('email')

        conexao_db.novo_Cliente(nome, cpf, logradouro, bairro, municipio,
                                   estado, cep, telefone, email)


@app.route('/clientes/<int:id>/', methods=['GET', 'POST'])
def getCliente(id):
    if request.method == 'GET':
        return conexao_db.get_cliente_by_id(id).toJson()
    if request.method == 'POST':
        pass
        # return render_template('Alterar_Produto.html', descricao=produto.descricao, codigo_barras = produto.codBarras, unidade_medida=produto.un, preco = produto.preco)

"""
@app.route('/estoque/')
def getEstoque():
    estoque = conexao_db.get_estoque_by_id()
    return json.dumps(estoque)
"""
@app.route('/estoque/add/', methods=['POST'])
def new_estoque():
    if request.method == 'POST':
        descricao = request.form.get('descricao')

        conexao_db.novo_estoque(descricao)

@app.route('/estoque/<int:id>/', methods=['GET', 'POST'])
def getEstoque(id):
    if request.method == 'GET':
        return conexao_db.get_estoque_by_id(id).toJson()
    if request.method == 'POST':
        pass
        # return render_template('Alterar_Produto.html', descricao=produto.descricao, codigo_barras = produto.codBarras, unidade_medida=produto.un, preco = produto.preco)

"""
@app.route('/estoque/saldo/')
def getEstoque():
    saldo_estoque = conexao_db.get_saldo_estoque_by_id(id)
    return json.dumps(estoque)
"""
@app.route('/estoque/saldo/add/', methods=['POST'])
def new_saldo_estoque():
    if request.method == 'POST':
        id_estoque = request.form.get('id_estoque')
        id_produto = request.form.get('id_produto')
        saldo = request.form.get('saldo')

        conexao_db.novo_saldo_inicial_estoque(id_estoque, id_produto, saldo)

@app.route('/estoque/saldo/<int:id>/', methods=['GET', 'POST'])
def getSaldoEstoque(id):
    if request.method == 'GET':
        return conexao_db.get_saldo_estoque_by_id(id).toJson()
    if request.method == 'POST':
        pass
        # return render_template('Alterar_Produto.html', descricao=produto.descricao, codigo_barras = produto.codBarras, unidade_medida=produto.un, preco = produto.preco)

"""
@app.route('/estoque/movimentacao/')
def getEstoque():
    saldo_estoque = conexao_db.get_saldo_estoque_by_id(id)
    return json.dumps(estoque)
"""

@app.route('/estoque/movimentacao/add/', methods=['POST'])
def new_saldo_movimentacao():
    if request.method == 'POST':
        id_estoque = request.form.get('id_estoque')
        id_produto = request.form.get('id_produto')
        origem = request.form.get('origem')
        tipo = request.form.get('tipo')
        quantidade = request.form.get('quantidade')

        conexao_db.nova_movimentacao_estoque(id_estoque, id_produto, tipo, quantidade, origem)


@app.route('/estoque/movimentacao/<int:id>/', methods=['GET', 'POST'])
def getSaldoEstoqueMovimento(id):
    if request.method == 'GET':
        return conexao_db.get_movimento_bancario_by_id(id).toJson()
        #tá errado isso aqui num ta não??
    if request.method == 'POST':
        pass
        # return render_template('Alterar_Produto.html', descricao=produto.descricao, codigo_barras = produto.codBarras, unidade_medida=produto.un, preco = produto.preco)

@app.route('/bancos/')
def getBancos():
    bancos = conexao_db.get_all_Bancos()
    bancos = [Banco.toJson() for Banco in bancos]
    return json.dumps(bancos)


@app.route('/bancos/add/', methods=['POST'])
def new_banco():
    if request.method == 'POST':
        codigo_bancario = request.form.get('codigo_bancario')
        nome = request.form.get('nome')
        agencia = request.form.get('agencia')
        conta = request.form.get('conta')
        logradouro = request.form.get('logradouro')
        bairro = request.form.get('bairro')
        municipio = request.form.get('municipio')
        estado = request.form.get('estado')
        cep = request.form.get('cep')
        telefone = request.form.get('telefone')
        email = request.form.get('email')
        saldo = request.form.get('saldo')

        conexao_db.novo_Banco(codigo_bancario, nome, agencia, conta, logradouro, bairro, municipio, estado, cep, telefone, email, saldo)


@app.route('/bancos/<int:id>/', methods=['GET', 'POST'])
def getBanco(id):
    if request.method == 'GET':
        return conexao_db.get_banco_by_id(id).toJson()
    if request.method == 'POST':
        pass
        # return render_template('Alterar_Produto.html', descricao=produto.descricao, codigo_barras = produto.codBarras, unidade_medida=produto.un, preco = produto.preco)

@app.route('/banco/movimento_bancario/add')
def new_movimento_bancario():
    if request.method == 'POST':
        id_banco = request.form.get('id_banco')
        tipo = request.form.get('tipo')
        origem = request.form.get('origem')
        valor = request.form.get('valor')
        dataMovimento = request.form.get('dataMovimento')

        conexao_db.nova_movimentacao_bancaria(id_banco, tipo, valor, origem)


@app.route('/banco/movimento_bancario/<int:id>/', methods=['GET', 'POST'])
def getSaldoEstoqueMovimento(id):
    if request.method == 'GET':
        return conexao_db.get_movimento_bancario_by_id(id).toJson()
        # tá errado isso aqui num ta não??
    if request.method == 'POST':
        pass
        # return render_template('Alterar_Produto.html', descricao=produto.descricao, codigo_barras = produto.codBarras, unidade_medida=produto.un, preco = produto.preco)

# Rota para a nota fiscal

@app.route('/nf/')
def getNf():
    nfs = conexao_db.get_all_NFS()
    nfs = [Nota_fiscal.toJson() for Nota_fiscal in nfs]
    return json.dumps(nfs)

@app.route('/nf/add/', methods=['POST'])
def new_nf():
    if request.method == 'POST':
        numero = request.form.get('numero')
        id_fornecedor = request.form.get('id_fornecedor')
        tipo = request.form.get('tipo')
        valor = request.form.get('valor')

        conexao_db.novo(numero, id_fornecedor, valor)


@app.route('/nf/<int:id>/', methods=['GET', 'POST'])
def getNf(id):
    if request.method == 'GET':
        return conexao_db.get_NF_by_id(id).toJson()
    if request.method == 'POST':
        pass
        # return render_template('Alterar_Produto.html', descricao=produto.descricao, codigo_barras = produto.codBarras, unidade_medida=produto.un, preco = produto.preco)

# Rota para o cabeçaljo da nota fiscal porém um pouco confusa essas duas

"""
@app.route('/nf/cabecalho/')
def getNfCabecalho():
    nf_cabecalho = conexao_db.get_NF_by_id()
    bancos = [Banco.toJson() for Banco in bancos]
    return json.dumps(bancos)
"""

@app.route('/nf/cabecalho/add/', methods=['POST'])
def new_nf_cabecalho():
    if request.method == 'POST':
        numero = request.form.get('numero')
        id_fornecedor = request.form.get('id_fornecedor')
        valor = request.form.get('valor')

        conexao_db.novo_cabecalho_NF(numero, id_fornecedor, valor)


@app.route('/nf/cabecalho/<int:id>/', methods=['GET', 'POST'])
def getNfCabecalho(id):
    if request.method == 'GET':
        return conexao_db.get_NF_by_id(id).toJson()
    if request.method == 'POST':
        pass
        # return render_template('Alterar_Produto.html', descricao=produto.descricao, codigo_barras = produto.codBarras, unidade_medida=produto.un, preco = produto.preco)

"""
@app.route('/nf/itens/')
def getNfCabecalho():
    nf_itens = conexao_db.get_itens_nf(id)
    bancos = [Banco.toJson() for Banco in bancos]
    return json.dumps(bancos)
"""

@app.route('/nf/itens/add/', methods=['POST'])
def new_nf_itens():
    if request.method == 'POST':
        tipo = request.form.get('tipo')
        id_cabecalho = request.form.get('id_cabecalho')
        id_produto = request.form.get('id_produto')
        valor = request.form.get('valor')
        quantidade = request.form.get('quantidade')

        conexao_db.novo_item_nf(tipo, id_cabecalho, id_produto, quantidade, valor)


@app.route('/nf/itens/<int:id>/', methods=['GET', 'POST'])
def getNfItens(id):
    if request.method == 'GET':
        return conexao_db.get_itens_nf(id).toJson()
    if request.method == 'POST':
        pass
        # return render_template('Alterar_Produto.html', descricao=produto.descricao, codigo_barras = produto.codBarras, unidade_medida=produto.un, preco = produto.preco)

conexao_db.create_data_base()
app.run()