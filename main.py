import json

from flask import Flask, request, render_template
from models.User import User
from util_db import conexao_db
from templates.formularios import FormularioLogin



app = Flask(__name__)
app.config.from_object('config')

@app.route('/', methods=['GET', 'POST'])
def mainPage():
        form = FormularioLogin()
        if form.validate_on_submit():
            User = conexao_db.get_user(form.user.data)
            if conexao_db.get_user(form.user.data):
                return 'erro'
            if (conexao_db.get_user(form.user.data)).senha == form.senha.data:
                return render_template("paginaInicial.html")
            print(form.user.data)
            print(form.senha.data)
        return render_template("login.html", form=form)

@app.route('/produtos/')
def getProdutos():
    produtos = conexao_db.get_all_Produtos()
    produtos = [Produto.toJson() for Produto in produtos]
    return json.dumps(produtos)

@app.route('/produtos/add/', methods=['GET','POST'])
def new_produto():
    if request.method == 'POST':
        descricao = request.form.get('descricao')
        preco = request.form.get('preco')
        unidade_medida = request.form.get('unidade_medida')
        codigo_barras = request.form.get('codigo_barras')

        conexao_db.novo_Produto(descricao,preco,unidade_medida,codigo_barras)

        return "post"

    if request.method == 'GET':
        return render_template('Cadastrar_produto.html')


@app.route('/produtos/<int:id>/', methods=['GET', 'POST'])
def getProduto(id):
    if request.method == 'GET':
        produto = conexao_db.get_produto_by_id(id)
        return render_template('Alterar_Produto.html', descricao=produto.descricao, codigo_barras = produto.codBarras, unidade_medida=produto.un, preco = produto.preco)
    #return produto.toJson()

@app.route('/fornecedor/')
def getFornecedorJson():
    #Modifiquei o nome desse
    return {
    'ID' : 1,
    'RazaoSocial' : 'FornecedorX',
    'NomeFantasia' : 'FornecedorX',
    'CNPJ' : '00.000.000/0000-00',
    'IE' : '00000000',
    'Endereco' : 'Rua XXX',
    'Bairro' : 'Bairro XXX',
    'Municipio' : 'Cidade XXX',
    'Estado' : 'PE',
    'CEP' : '00000000',
    'Telefone' : '00000000000',
    'Email' : 'XXX@gmail.com'
    }

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

        return "post"

    if request.method == 'GET':
        return render_template('Cadastrar_fornecedor.html')

@app.route('/fornecedores/<int:id>/', methods=['GET', 'POST'])
def getFornecedor(id):
    if request.method == 'GET':
        fornecedor = conexao_db.get_fornecedor_by_id(id)
        return render_template('alterar_fornecedor.html', razao_social=fornecedor.razao_social, nome_fantasia=fornecedor.nome_fantasia, cnpj=fornecedor.cnpj, inscricao_estadual=fornecedor.inscricao_estadual, logradouro=fornecedor.logradouro, bairro=fornecedor.bairro, municipio=fornecedor.municipio, estado=fornecedor.estado, cep=fornecedor.cep, telefone=fornecedor.telefone,  email=fornecedor.email)
    #return fornecedor.toJson()

@app.route('/cliente/')
def getClientes():
    return {
    'ID' : 1,
    'Nome' : 'ClienteX',
    'CPF' : '000.000.000-00',
    'Endereco' : 'Rua XXX',
    'Bairro' : 'Bairro XXX',
    'Municipio' : 'Cidade XXX',
    'Estado' : 'PE',
    'CEP' : '00000000',
    'Telefone' : '00000000000',
    'Email' : 'XXX@gmail.com'
    }

@app.route('/estoque/')
def getEstoque():

    return {
    'ID' : 1,
    'Descricao' : 'EstoqueX'
    }

@app.route('/estoque/saldo/')
def getSaldo():
    return {
    'ID' : 1,
    'Produto' : '00',
    'Estoque' : '00',
    'Saldo' : 0
    }

@app.route('/estoque/movimentacao/')
def getMovimentacao():
    return {
    'ID' : 1,
    'Produto' : '00',
    'Estoque' : '00',
    'Origem': '00',
    'Tipo': 'Entrada',
    'Quantidade' : 0
    }

@app.route('/banco/')
def getBanco():
    return {
    'ID' : 1,
    'Banco' : 'Codigo do BancoX',
    'NomeBanco' : 'Bradesco',
    'Agencia' : '0651',
    'Conta' : '0000',
    'Endereco' : 'Rua X',
    'Bairro' : 'Bairro XXX',
    'Municipio' : 'Cidade XXX',
    'Estado' : 'PE',
    'CEP' : '00000000',
    'Telefone' : '00000000000',
    'Email' : 'XXX@gmail.com',
    'Saldo' : 0.00,
    'DataFechamento' : '31/10/2021',
    }

@app.route('/banco/titulo/')
def getTitulo():
    return{
    'ID' : 1,
    'Banco' : 237,
    'Conta' : '00000',
    'Tipo' : 'Receber',
    'Origem' : 'FiadoClienteX',
    'Valor' : 0,
    'Vencimento' : '30/11/2021',
    'Status' : 'Pendente'
    }

@app.route('/banco/movimento_bancario/')
def getMovimentoBancario():
    return{
    'ID' : 1,
    'Banco' : 237,
    'Conta' : '00000',
    'Tipo' : 'Receber',
    'Origem' : 'FiadoClienteX',
    'Valor' : 0,
    'DataMovimento' : '30/11/2021',
    }

@app.route('/nf/cabecalho/')
def getNFCabecalho():
    return{
    'ID' : 1,
    'Numero' : 123,
    'Fornecedor' : 1,
    'Tipo' : 'Entrada',
    'Valor' : 0.00,
    'Data' : '31/10/2021',
    'Vencimento':'30/11/2021'
    }

@app.route('/nf/itens/')
def getNFItens():
    return{
    'ID' : 1,
    'Origem' : 123,
    'Fornecedor': 1,
    'tipo' : 'Entrada',
    'Produto':'01',
    'Quantidade' :1,
    'Valor' : 0,
    'Data' : '31/10/2021',
    }

conexao_db.create_data_base()
app.run()