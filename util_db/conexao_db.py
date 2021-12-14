from locale import str
from models.Produto import Produto
from models.User import User
from models.Fornecedor import Fornecedor
from models.Cliente import Cliente
from models.Estoque import Estoque
from models.Saldo_Estoque import Saldo_Estoque
from models.Banco import Banco
from models.Movimento_Bancario import Movimento_Bancario
from models.Titulo_Bancario import Titulo_Bancario
from models.Nota_Fiscal import Nota_Fiscal
from models.Item_NF import Item_NF
from models.item_venda import Item_Venda
from models.Venda import Venda

import psycopg2

#Dados da conecção
concect = psycopg2.connect(
    host = 'localhost',
    database = 'hermes',
    user = 'postgres',
    password = 'matheus19dev',

)


#Criando banco de dados
def create_table_Users():
    cursor = concect.cursor()
    table = 'create table if not exists Users(id serial primary key, usuario varchar(20) UNIQUE, senha varchar(50), nivel_acesso Int)'
    cursor.execute(table)
    concect.commit()
    cursor.close()

def create_table_Produto():
    cursor = concect.cursor()
    table = 'create table if not exists Produto(id serial primary key, descricao varchar(255), preco REAL, unidade_medida varchar(2), codigo_barras varchar(13))'
    cursor.execute(table)
    concect.commit()
    cursor.close()

def create_table_Fornecedor():
    cursor = concect.cursor()
    table = 'create table if not exists Fornecedor(id serial PRIMARY KEY, razao_social varchar(255), nome_fantasia varchar(255), cnpj varchar(14) UNIQUE, inscricao_estadual varchar(9) UNIQUE, logradouro varchar(255), bairro varchar(32), municipio varchar(32), estado varchar(2), cep varchar(8), telefone varchar(11), email varchar(255))'
    cursor.execute(table)
    concect.commit()
    cursor.close()

def create_table_Cliente():
    cursor = concect.cursor()
    table = 'create table if not exists Cliente(id serial PRIMARY KEY, nome varchar(255), cpf varchar(11) UNIQUE, logradouro varchar(255), bairro varchar(32), municipio varchar(32), estado varchar(2), CEP varchar(8), telefone varchar(11), email varchar(255))'
    cursor.execute(table)
    concect.commit()
    cursor.close()

def create_table_Estoque():
    cursor = concect.cursor()
    table = 'create table if not exists Estoque(id serial primary key, descricao varchar(255))'
    cursor.execute(table)
    concect.commit()
    cursor.close()

def create_table_Saldo_Estoque():
    cursor = concect.cursor()
    table = 'create table if not exists Saldo_Estoque(id serial primary key, produto INTEGER references Produto(id), estoque INTEGER references Estoque(id), saldo REAL)'
    cursor.execute(table)
    concect.commit()
    cursor.close()

def create_table_Movimento_Estoque():
    cursor = concect.cursor()
    table = 'create table if not exists Movimento_Estoque(id serial primary key, origem varchar(9), tipo varchar(1), produto INTEGER references Produto(id), estoque INTEGER references Estoque(id), quantidade REAL, dataMovimento Date)'
    cursor.execute(table)
    concect.commit()
    cursor.close()

def create_table_Banco():
    cursor = concect.cursor()
    table = 'create table if not exists Banco( id serial primary key, codigoBancario varchar(3), nomeBanco varchar(50),	agencia varchar(4), conta varchar(12) UNIQUE, endereco varchar(50), bairro varchar(15), municipio varchar(15), estado varchar(2), cep varchar(8), telefone varchar(11), email varchar(50), saldo REAL)'
    cursor.execute(table)
    concect.commit()
    cursor.close()

def create_table_Movimento_Bancario():
    cursor = concect.cursor()
    table = 'create table if not exists Movimento_Bancario(id serial primary key, banco INTEGER references Banco(id), tipo varchar(7), origem varchar(15), valor REAL, dataMovimento Date)'
    cursor.execute(table)
    concect.commit()
    cursor.close()

def create_table_Titulo_Bancario():
    cursor = concect.cursor()
    table = 'create table if not exists Titulo_Bancario(id serial primary key, banco INTEGER references Banco(id), tipo varchar(7), origem varchar(15), valor REAL, vencimento Date, status varchar(8),	movimento INTEGER references Movimento_Bancario(id))'
    cursor.execute(table)
    concect.commit()
    cursor.close()

def create_table_Nota_Fiscal():
    cursor = concect.cursor()
    table = 'create table if not exists Nota_Fiscal(id serial primary key, numero varchar(9), fornecedor INTEGER references Fornecedor(id), tipo varchar(7), valor REAL, dataEntrada Date, tituloBancario INTEGER references Titulo_Bancario(id))'
    cursor.execute(table)
    concect.commit()
    cursor.close()

def create_table_Item_NF():
    cursor = concect.cursor()
    table = 'create table if not exists Item_NF(id serial primary key, origem INTEGER references Nota_Fiscal(id), fornecedor INTEGER references Fornecedor(id), tipo varchar(7), produto INTEGER references Produto(id), quantidade REAL, valor REAL, dataEntrada Date)'
    cursor.execute(table)
    concect.commit()
    cursor.close()

def create_table_Venda():
    cursor = concect.cursor()
    table = 'create table if not exists Venda(id serial primary key, total REAL, cliente INTEGER references Cliente(id), data Date)'
    cursor.execute(table)
    concect.commit()
    cursor.close()

def create_table_item_Venda():
    cursor = concect.cursor()
    table = 'create table if not exists Item_Venda(id serial primary key, produto INTEGER references Produto(id), quantidade REAL, preco REAL, venda INTEGER references Venda(id))'
    cursor.execute(table)
    concect.commit()
    cursor.close()

def create_data_base():
    create_table_Users()
    create_table_Produto()
    create_table_Fornecedor()
    create_table_Cliente()
    create_table_Estoque()
    create_table_Saldo_Estoque()
    create_table_Movimento_Estoque()
    create_table_Banco()
    create_table_Movimento_Bancario()
    create_table_Titulo_Bancario()
    create_table_Nota_Fiscal()
    create_table_Item_NF()
    create_table_Venda()
    create_table_item_Venda()
    get_all_Users()

#Funções de inserção

#Cadastros
def novo_User(usuario, senha, nivel_acesso):
    cursor = concect.cursor()
    novoRegistro = "insert into Users(usuario, senha, nivel_acesso) values ('"+usuario+"', '"+senha+"', '"+nivel_acesso+"')"
    cursor.execute(novoRegistro)
    concect.commit()
    cursor.close()

def novo_Produto(descricao, preco, un, codBarras):
    cursor = concect.cursor()
    novoRegistro = "insert into produto(descricao, preco, unidade_medida, codigo_barras) values ('"+descricao+"', "+str(preco)+", '"+un+"', '"+codBarras+"') "
    cursor.execute(novoRegistro)
    concect.commit()
    cursor.close()

def novo_Banco(codigobancario,  nomebanco, agencia,  conta,  endereco, bairro, municipio, estado, cep, telefone,  email,  saldo):
    cursor = concect.cursor()
    novoRegistro = "insert into banco(codigobancario, nomebanco, agencia, conta, endereco, bairro, municipio, estado, cep, telefone, email, saldo) values ('"+codigobancario+"', "+nomebanco+", '"+agencia+"', '"+conta+", '"+endereco+", '"+bairro+", '"+municipio+", '"+estado+", '"+cep+", '"+telefone+", '"+email+", '"+str(saldo)+"') "
    cursor.execute(novoRegistro)
    concect.commit()
    cursor.close()

def novo_Cliente(nome,  cpf, logradouro, bairro, municipio, estado, cep, telefone,  email,  saldo):
    cursor = concect.cursor()
    novoRegistro = "insert into Cliente(nome, cpf,  logradouro, bairro, municipio, estado, cep, telefone, email, saldo) values ('"+nome+"', "+cpf+", '"+logradouro+", '"+bairro+", '"+municipio+", '"+estado+", '"+cep+", '"+telefone+", '"+email+", '"+str(saldo)+"') "
    cursor.execute(novoRegistro)
    concect.commit()
    cursor.close()

def novo_Fornecedor(razao_social, nome_fantasia, cnpj, inscricao_estadual, logradouro, bairro, municipio, estado, cep, telefone,  email,  saldo):
    cursor = concect.cursor()
    novoRegistro = "insert into Fornecedor(razao_social, nome_fantasia, cnpj, inscricao_estaudal,  logradouro, bairro, municipio, estado, cep, telefone, email, saldo) values ('"+razao_social+"', "+nome_fantasia+"', "+cnpj+"', "+inscricao_estadual+", '"+logradouro+", '"+bairro+", '"+municipio+", '"+estado+", '"+cep+", '"+telefone+", '"+email+", '"+str(saldo)+"') "
    cursor.execute(novoRegistro)
    concect.commit()
    cursor.close()

def novo_estoque(descricao):
    cursor = concect.cursor()
    novoRegistro = "insert into estoque(descricao) values ('"+descricao+"') "
    cursor.execute(novoRegistro)
    concect.commit()
    cursor.close()

def novo_saldo_inicial_estoque(estoque, produto):
    pass
#Funções de recuperação de dados

def get_all_Users():
    cursor = concect.cursor()
    novoUser = "SELECT * from Users"
    cursor.execute(novoUser)
    lista = []
    data_manager = cursor.fetchone()
    if data_manager is None:
        novo_User("admin", "admin", "3")
    while data_manager is not None:
        lista.append(User(data_manager[0], data_manager[1], data_manager[2], data_manager[3]))
        data_manager = cursor.fetchone()

    return lista

def get_user(userStr):
    cursor = concect.cursor()
    buscarUser = "SELECT * from Users where usuario='"+userStr+"'"
    cursor.execute(buscarUser)
    data_manager = cursor.fetchone()
    if data_manager:
        return (User(data_manager[0], data_manager[1],  data_manager[2], data_manager[3]))
    else:
        return None

def get_all_Produtos():
    cursor = concect.cursor()
    novoProduto = "SELECT * from Produto"
    cursor.execute(novoProduto)
    lista_produtos = []
    data_manager = cursor.fetchone()

    while data_manager is not None:
        lista_produtos.append(Produto(data_manager[0], data_manager[1], data_manager[2], data_manager[3], data_manager[4]))
        data_manager = cursor.fetchone()

    return lista_produtos

def get_produto_by_id(id):
    cursor = concect.cursor()
    novoProduto = "SELECT * from Produto where id="+str(id)
    cursor.execute(novoProduto)
    data_manager = cursor.fetchone()

    if data_manager is not None:
        return Produto(data_manager[0], data_manager[1], data_manager[2], data_manager[3], data_manager[4])

    return None

def get_all_Fornecedores():
        cursor = concect.cursor()
        novoFornecedor = "SELECT * from Fornecedor"
        cursor.execute(novoFornecedor)
        lista_fornecedores = []
        data_manager = cursor.fetchone()

        while data_manager is not None:
            lista_fornecedores.append(
                Fornecedor(data_manager[0], data_manager[1], data_manager[2], data_manager[3], data_manager[4], data_manager[5], data_manager[6], data_manager[7], data_manager[8], data_manager[9], data_manager[10], data_manager[11]))
            data_manager = cursor.fetchone()

        return lista_fornecedores

def get_fornecedor_by_id(id):
        cursor = concect.cursor()
        novoFornecedor = "SELECT * from Fornecedor where id=" + str(id)
        cursor.execute(novoFornecedor)
        data_manager = cursor.fetchone()

        if data_manager is not None:
            return Fornecedor(data_manager[0], data_manager[1], data_manager[2], data_manager[3], data_manager[4], data_manager[5], data_manager[6], data_manager[7], data_manager[8], data_manager[9], data_manager[10], data_manager[11])

        return None

def get_all_Clientes():
        cursor = concect.cursor()
        novoCliente = "SELECT * from Cliente"
        cursor.execute(novoCliente)
        lista_clientes = []
        data_manager = cursor.fetchone()

        while data_manager is not None:
            lista_clientes.append(
                Cliente(data_manager[0], data_manager[1], data_manager[2], data_manager[3], data_manager[4], data_manager[5], data_manager[6], data_manager[7], data_manager[8], data_manager[9]))
            data_manager = cursor.fetchone()

        return lista_clientes

def get_cliente_by_id(id):
        cursor = concect.cursor()
        novoCliente = "SELECT * from Cliente where id=" + str(id)
        cursor.execute(novoCliente)
        data_manager = cursor.fetchone()

        if data_manager is not None:
            return Cliente(data_manager[0], data_manager[1], data_manager[2], data_manager[3], data_manager[4], data_manager[5], data_manager[6], data_manager[7], data_manager[8], data_manager[9])

        return None

def get_all_Estoques():
    cursor = concect.cursor()
    novoEstoque = "SELECT * from Estoque"
    cursor.execute(novoEstoque)
    lista_estoques = []
    data_manager = cursor.fetchone()

    while data_manager is not None:
        lista_estoques.append(
            Estoque(data_manager[0], data_manager[1]))
        data_manager = cursor.fetchone()

    return lista_estoques

def get_estoque_by_id(id):
    cursor = concect.cursor()
    novoEstoque = "SELECT * from Estoque where id=" + str(id)
    cursor.execute(novoEstoque)
    data_manager = cursor.fetchone()

    if data_manager is not None:
        return Estoque(data_manager[0], data_manager[1])

    return None

def get_saldo_estoque_by_estoque_e_produto(produto, estoque):
    cursor = concect.cursor()
    novoSaldo = "SELECT * from Saldo_Estoque where produto=" + str(produto) + " and estoque="+ str(estoque)
    cursor.execute(novoSaldo)
    lista_saldo = []
    data_manager = cursor.fetchone()

    while data_manager is not None:
        lista_saldo.append(
            Saldo_Estoque(data_manager[0], data_manager[1], data_manager[2], data_manager[3]))
        data_manager = cursor.fetchone()

    return lista_saldo

def get_saldo_estoque_by_id(id):
    cursor = concect.cursor()
    novoSaldo = "SELECT * from Saldo_Estoque where id=" + str(id)
    cursor.execute(novoSaldo)
    data_manager = cursor.fetchone()

    if data_manager is not None:
        return Saldo_Estoque(data_manager[0], data_manager[1], data_manager[2],  data_manager[3])

    return None

def get_all_Bancos():
        cursor = concect.cursor()
        novoBanco = "SELECT * from Banco"
        cursor.execute(novoBanco)
        lista_bancos = []
        data_manager = cursor.fetchone()

        while data_manager is not None:
            lista_bancos.append(
                Banco(data_manager[0], data_manager[1], data_manager[2], data_manager[3], data_manager[4], data_manager[5], data_manager[6], data_manager[7], data_manager[8], data_manager[9], data_manager[10], data_manager[11]))
            data_manager = cursor.fetchone()

        return lista_bancos

def get_banco_by_id(id):
        cursor = concect.cursor()
        novoBanco = "SELECT * from Banco where id=" + str(id)
        cursor.execute(novoBanco)
        data_manager = cursor.fetchone()

        if data_manager is not None:
            return Banco(data_manager[0], data_manager[1], data_manager[2], data_manager[3], data_manager[4], data_manager[5], data_manager[6], data_manager[7], data_manager[8], data_manager[9], data_manager[10], data_manager[11])

        return None

def get_movimentos_bancario_by_banco(banco):
    cursor = concect.cursor()
    novoMovimento = "SELECT * from Movimento_Bancario where Banco=" + str(banco)
    cursor.execute(novoMovimento)
    lista_movimentos = []
    data_manager = cursor.fetchone()

    while data_manager is not None:
        lista_movimentos.append(
            Movimento_Bancario(data_manager[0], data_manager[1], data_manager[2], data_manager[3], data_manager[4], data_manager[5]))
        data_manager = cursor.fetchone()

    return lista_saldo

def get_movimento_bancario_by_id(id):
    cursor = concect.cursor()
    novoMovimento = "SELECT * from Movimento_Bancario where id=" + str(id)
    cursor.execute(novoMovimento)
    data_manager = cursor.fetchone()

    if data_manager is not None:
        return Movimento_Bancario(data_manager[0], data_manager[1], data_manager[2], data_manager[3], data_manager[4], data_manager[5])

    return None

def get_titulos_bancario_by_status(status):
        cursor = concect.cursor()
        if status=='todos':
            novoTitulo = "SELECT * from Titulo_Bancario"
        else:
            novoTitulo = "SELECT * from Titulo_Bancario where status=" + str(status)
        cursor.execute(novoTitulo)
        lista_titulos = []
        data_manager = cursor.fetchone()

        while data_manager is not None:
            lista_titulos.append(
                Titulo_Bancario(data_manager[0], data_manager[1], data_manager[2], data_manager[3], data_manager[4],
                                   data_manager[5], data_manager[6], data_manager[7]))
            data_manager = cursor.fetchone()

        return lista_titulos

def get_titulo_bancario_by_id(id):
        cursor = concect.cursor()
        novoTitulo = "SELECT * from Titulo_Bancario where id=" + str(id)
        cursor.execute(novoTitulo)
        data_manager = cursor.fetchone()

        if data_manager is not None:
            return Titulo_Bancario(data_manager[0], data_manager[1], data_manager[2], data_manager[3], data_manager[4],
                                   data_manager[5], data_manager[6], data_manager[7])

        return None

def get_all_NFS():
    cursor = concect.cursor()
    novaNF = "SELECT * from Nota_Fiscal"
    cursor.execute(novaNF)
    lista_nfs = []
    data_manager = cursor.fetchone()

    while data_manager is not None:
        lista_nfs.append(
            Nota_Fiscal(data_manager[0], data_manager[1], data_manager[2], data_manager[3], data_manager[4], data_manager[5],
                  data_manager[6]))
        data_manager = cursor.fetchone()

    return lista_nfs

def get_NF_by_id(id):
    cursor = concect.cursor()
    novaNF = "SELECT * from Nota_Fiscal where id=" + str(id)
    cursor.execute(novaNF)
    data_manager = cursor.fetchone()

    if data_manager is not None:
        return Nota_Fiscal(data_manager[0], data_manager[1], data_manager[2], data_manager[3], data_manager[4],
                     data_manager[5], data_manager[6])

    return None

def get_itens_nf(id_nf):
    cursor = concect.cursor()
    novoItem = "SELECT * from Item_nf where origem="+id_nf
    cursor.execute(novoItem)
    lista_itens = []
    data_manager = cursor.fetchone()

    while data_manager is not None:
        lista_itens.append(
            Item_NF(data_manager[0], data_manager[1], data_manager[2], data_manager[3], data_manager[4], data_manager[5],
                  data_manager[6], data_manager[7]))
        data_manager = cursor.fetchone()

    return lista_itens

def get_all_Vendas():
    cursor = concect.cursor()
    novaVenda = "SELECT * from Venda"
    cursor.execute(novaVenda)
    lista_Vendas = []
    data_manager = cursor.fetchone()

    while data_manager is not None:
        lista_Vendas.append(
            Venda(data_manager[0], data_manager[1], data_manager[2], data_manager[3]))
        data_manager = cursor.fetchone()

    return lista_Vendas

def get_Venda_by_id(id):
    cursor = concect.cursor()
    novaVenda = "SELECT * from Venda where id=" + str(id)
    cursor.execute(novaVenda)
    data_manager = cursor.fetchone()

    if data_manager is not None:
        return Venda(data_manager[0], data_manager[1], data_manager[2], data_manager[3])

    return None

def get_itens_Venda(id_venda):
    cursor = concect.cursor()
    novoItem = "SELECT * from item_venda where venda="+id_venda
    cursor.execute(novoItem)
    lista_itens = []
    data_manager = cursor.fetchone()

    while data_manager is not None:
        lista_itens.append(
            Item_Venda(data_manager[0], data_manager[1], data_manager[2], data_manager[3], data_manager[4]))
        data_manager = cursor.fetchone()

    return lista_itens