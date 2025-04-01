# Add whatever it is needed to interface with the DB Table corso
from oauthlib.uri_validate import query

from database.DB_connect import DBConnect
from model.corso import Corso
from model.studente import Studente
from database.studente_DAO import StudentiDAO

class CorsiDAO:

    def getAllCorsi(self):

        cnx= DBConnect.get_connection()

        cursor=cnx.cursor(dictionary=True)

        query="""select * from corso"""
        cursor.execute(query)

        res=[]
        for row in cursor:
            res.append(Corso(row["codins"],row["crediti"],row["nome"],row["pd"]))

        cnx.close()
        return res

    def getIscritti(self,codiceCorso):
        cnx = DBConnect.get_connection()

        cursor = cnx.cursor(dictionary=True)

        # query = f"""select matricola
        #             from iscrizione
        #             where codins="{codiceCorso}" """
        # cursor.execute(query)
        query = f"""SELECT matricola 
                    FROM iscrizione 
                    WHERE codins ="{codiceCorso}" """
        cursor.execute(query)
        result = cursor.fetchall() #RESTITUISCE UNA LISTA DELLA QUERY ESEGUITA

        res = []
        dao=StudentiDAO()
        studenti=dao.getAllStudenti()
        for m in result:
            for s in studenti:
                if m["matricola"]==s._matricola:
                    res.append(s)

        cursor.close()
        cnx.close()
        return res

    def getCorsiMatricola(self,matricola):
        cnx=DBConnect.get_connection()
        cursor=cnx.cursor(dictionary=True)
        query=f"""SELECT codins FROM iscrizione WHERE matricola={matricola} """
        cursor.execute(query)
        result=cursor.fetchall()

        corsi=self.getAllCorsi()
        res=[]
        for c in result:
            for x in corsi:
                if c["codins"]==x._codice:
                    res.append(x)

        cursor.close()
        cnx.close()
        return res

    def addStudente(self,matricola,cod):
        cnx=DBConnect.get_connection()
        cursor=cnx.cursor()
        query=f"""INSERT INTO iscrizione (matricola, codins)
                SELECT * FROM (SELECT {matricola} AS matricola, '{cod}' AS codins) AS tmp
                WHERE NOT EXISTS (
                SELECT 1 FROM iscrizione WHERE matricola = {matricola} AND codins = '{cod}'
                );"""

        cursor.execute(query)

        cursor.close()
        cnx.commit()
        cnx.close()
        return
