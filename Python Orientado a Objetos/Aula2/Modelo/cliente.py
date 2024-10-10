from abc import ABC, abstractmethod

class Cliente(ABC):

    @abstractmethod
    def calcular_desconto(self):
        pass

        def __init__(self, nome = None, email = None):
            self._nome = nome
            self._email = email

            pass

        @property
        def nome(self):
            return self._nome
        @nome.setter
        def nome(self, value):
            self._nome= value
            pass


        @property
        def email(self):
            return self._email


        @email.setter
        def email(self, value):
            self._email = value
            pass

        def __str__(self):
         return f'{self._nome}, {self._email}'

class ClienteFisico(Cliente):

    def calcular_desconto(self):
        return 20.0

    def __init__(self, nome = None, email= None, cpf = None, sexo = None):
        Cliente.__init__(self, nome, email)
        self._cpf = cpf
        self._sexo = sexo
        pass

    @property
    def cpf(self):
        return self._cpf
    @cpf.setter
    def cpf(self, value):
        self._cpf = value
        pass

    @property
    def sexo(self):
        return self._sexo

    @sexo.setter
    def sexo(self, value):
        self._sexo = value
        pass

    def __str__(self):
        return f'{Cliente.__str__(self)},{self._cpf}, {self._sexo}'
        pass


class ClienteJuridico(Cliente):

    def calcular_desconto(self):
        return 30.0

    def __init__(self, nome = None, email = None, cnpj = None, ramo = None):
        Cliente. __init__(self, nome, email)
        self._cnpj = cnpj
        self._ramo = ramo

@property
def cnpj(self):
    return self._cnpj

@cnpj.setter
def cnpj(self, value):
    self._cnpj = value
    pass

@property
def ramo(self):
    return self._ramo

@ramo.setter
def ramo(self, value):
    self._ramo = value
    pass

def __str__(self):
    return f'{self._cnpj}, {self._ramo},{Cliente.__str__(self)}'
pass