class Produto:

    def __init__(self, nome=None, preco= None, quantidade= None):
        self._nome = nome
        self._preco = preco
        self._quantidade = quantidade

#SETTERS AND GETTERS

    @property
    def nome(self):
        return self._nome
    pass

    @nome.setter
    def nome(self, value):
        self._nome = value
    pass

    @property
    def preco(self):
        return self._preco
    pass

    @preco.setter
    def preco(self, value):
        self._preco = value
    pass

    @property
    def quantidade(self):
        return self._quantidade
    pass

    @quantidade.setter
    def quantidade(self, value):
        self._quantidade = value
    pass

    def __str__(self):
        return f'{self._nome}, {self._preco},{self._quantidade}'
    pass
