from banco.produto_dao import ProdutoDao

def cadastrar():
    try:
        produto = Produto(nome='Copo', preco= 12.0, quantidade = 3)
        dao = ProdutoDao()
        dao.create(produto)
        print('Produto Cadastrado com sucesso')

    except Exception as ex:
        print (ex)

    pass

def listar():
    try:
        dao = ProdutoDao()
        for produto in dao.read():
            print (produto)
    except Exception as ex:
        print (ex)
    pass

if __name__ == '__main__':

    #cadastrar
    listar()
    pass