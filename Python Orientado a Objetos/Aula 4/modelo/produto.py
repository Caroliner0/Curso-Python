class Produto:

    def __init__ (self, codigo = None, nome = None, preco = None, quantidade = None):
        self._codigo = codigo
        self._nome = nome
        self._preco = preco
        self._quantidade = quantidade
        pass


    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, value):
        self._codigo = value
    pass


    @property
    def preco(self):
        return  self._preco

    @preco.setter
    def preco(self, value):
        self._preco = value

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value
    pass


    @property
    def quantidade(self):
        return self._quantidade


    @quantidade.setter
    def quantidade(self, value):
        self._quantidade = value
    pass


    def __str__(self):
        return f'{self.codigo}, {self.nome}, {self.preco}, {self.quantidade}'

    def __repr__(self):
        return f'{self.codigo}, {self.nome}, {self.preco}, {preco.quantidade}'
    pass



