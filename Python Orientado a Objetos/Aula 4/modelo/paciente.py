class Paciente:

    def __init__(self, nome=None, sexo=None, idade=None):
        self.nome = nome
        self._idade = idade
        self._sexo = sexo
        # Atributo relacional 
        self._medicos = None

    @property
    def medicos(self):
        return self._medicos

    @medicos.setter
    def medicos(self, value):
        self._medicos = value
        pass

    @property
    def sexo(self):
        return self._sexo

    @sexo.setter
    def sexo(self, value):
        self._sexo = value
        pass

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, value):
        self._idade = value
        pass

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome (self, value):
        self._nome = value
        pass

    def __str__(self):
        return f'{self.nome}, {self.idade}, {self.sexo}'

    def __repr__(self):
        return f'{self.nome}, {self.idade}, {self.sexo}'

    pass