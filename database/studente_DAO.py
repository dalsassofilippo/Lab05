# Add whatever it is needed to interface with the DB Table studente
from contextlib import nullcontext

from oauthlib.uri_validate import query

from database.DB_connect import DBConnect
from model.studente import Studente


class StudentiDAO:


    def getAllStudenti(self):
        cnx=DBConnect.get_connection()

        cursor=cnx.cursor(dictionary=True)

        query="""select * from studente"""

        cursor.execute(query)

        res=[]

        for s in cursor:
            res.append(Studente(s["matricola"],s["cognome"],s["nome"],s["CDS"]))

        cnx.close()
        return res

