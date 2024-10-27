class Medico:

    def __init__(self, nome=None, especializacao=None):
        self._nome = nome
        self._especializacao = especializacao
        self._pacientes = None
        pass

    @property
    def pacientes(self):
        return self._pacientes

    @pacientes.setter
    def pacientes(self, value):
        self._pacientes = value
        pass


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self.nome = value
        pass

    @property
    def especializacao(self):
        return self._especializacao

    @especializacao.setter
    def especializacao(self, value):
        self._especializacao = value
        pass

    def __str__(self):
        return f'{self._nome}, {self._especializacao}'

    def __repr__(self):
        return f'{self._nome}, {self._especializacao}'

    pass