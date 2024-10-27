import psycopg2
class Connect:

    conn = None

    _database = 'aulap'
    _host = 'localhost'
    _user = 'postgres'
    _password = 'C@rol230398'



    def open (self):
        try:
            self.conn = psycopg2connect(host= self._host,
                                        user = self._user,
                                        password = self._password,
                                        dbname = self._database)
        except Exception as ex:
            raise Exception ('OpenError, erro ao abrir conexão.' + str (ex.args))
        pass

    def close (self):
        try:
            if self.conn is not None:
                self.conn.close()
            else:
            raise Exception ('CloseError, conexão nao foi aberta.')


        except Exception as ex:
            raise Exception ('CloseError, error ao fechar conexão.' +str(ex.args))


    pass