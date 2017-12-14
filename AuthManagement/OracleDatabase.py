import cx_Oracle
import traceback

class OracleDatabase():

    def get_connection(self):
        try:
            self.ip = '192.168.1.0'
            self.port = 1521
            self.SID = 'TESTEBS'
            self. dsn_tns = cx_Oracle.makedsn(self.ip, self.port, self.SID)

            db = cx_Oracle.connect('apps', 'sppa', self.dsn_tns)
        except:
            traceback.print_exc()
