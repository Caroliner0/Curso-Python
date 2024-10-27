from .connect import Connect

class ProdutoDao(Connect):

    def create(self, produto):
        try:
            self.open ()
            cursor = self.conn.cursor()
            cursor.execute('INSERT INTO product (nome, preco, quantidade) VALUES (%s, %s, %s)',
                           (produto.nome, produto.preco, produto.quantodade))
            self.conn.commit()

        finally:
            self.close()


        pass

    def read(self):
        try:
            self.open()
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM produto ORDER BY nome")
            registros = cursor.fetchall()
            produtos = []

            for registro in registros:
                produto = Produto(registro[0], registro [1], registro [2], registro [3])

            produtos.append(produto)

            return produtos

        except Exception as ex:
            raise Exception ('ReadError, erro ao ler os dados.' +str (ex.args))

        finally:
            self.close()



            pass

    def read_one(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass

