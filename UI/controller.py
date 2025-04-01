import flet as ft
from networkx.drawing import draw_kamada_kawai

from database.corso_DAO import CorsiDAO
from database.studente_DAO import StudentiDAO

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCercaIscritti(self, e):
        self._view._txt_result.controls.clear() #CANCELLA LA LISTVIEW
        self._view.update_page()
        cod = self._view._corso.value
        if cod is None or cod == "":
            self._view.create_alert("Selezionare un corso!")
            return
        dao=CorsiDAO()
        iscritti=dao.getIscritti(cod)
        self._view._txt_result.controls.append(ft.Text(f"Ci sono {len(iscritti)} iscritti al corso:"))
        for s in iscritti:
            self._view._txt_result.controls.append(ft.Text(f"{s.__str__()}"))
        self._view._txt_result.controls.append(ft.Text(""))
        self._view.update_page()

    def handleCercaStudente(self,e):
        matricola=self._view._txt_matricola.value
        if matricola is None or matricola=="":
            self._view.create_alert("Selezionare matricola!")
            self._view.update_page()
            return
        dao=StudentiDAO()
        studenti=dao.getAllStudenti()
        flag=False
        if matricola.isdigit(): # PER CONVERTIRE UNA STRINGA IN UN INTERO
            m=int(matricola)
            for s in studenti:
                if s._matricola==m:
                    self._view._txt_nome.value=s._nome
                    self._view._txt_cognome.value = s._cognome
                    flag=True
        else:
            self._view.create_alert("Attenzione la matricola deve essere di tipo numerico!")

        if flag==False:
            self._view.create_alert("Matricola non presente!")
            self._view.update_page()
            return
        self._view.update_page()


    def handleCercaCorsi(self,e):
        self._view._txt_result.controls.clear()
        self._view.update_page()
        matricola=self._view._txt_matricola.value
        dao = StudentiDAO()
        studenti = dao.getAllStudenti()
        flag = False
        if matricola.isdigit():
            m=int(matricola)
            for s in studenti:
                if s._matricola==m:
                    flag=True
        if flag==False:
            self._view.create_alert("Matricola non presente!")
            self._view.update_page()
            return
        dao1=CorsiDAO()
        corsi=dao1.getCorsiMatricola(matricola)
        self._view._txt_result.controls.append(ft.Text(f"Risultano {len(corsi)} corsi:"))
        for c in corsi:
            self._view._txt_result.controls.append(ft.Text(c.__str__()))
        self._view.update_page()


    def handleIscrivi(self,e):
        matricola = self._view._txt_matricola.value
        codice=self._view._corso.value

        dao = StudentiDAO()
        if matricola.isdigit():
            studenti = dao.getAllStudenti()
            studente = None
            m = int(matricola)
            for s in studenti:
                if s._matricola == m:
                    studente=s

            dao1=CorsiDAO()

            corsi = dao1.getCorsiMatricola(m)
            flag = True
            for x in corsi:
                if x._codice == codice:
                    flag = False
            if flag==True:
                dao1.addStudente(m, codice)
            else:
                self._view.create_alert("Matricola già iscritta al corso!")
                self._view.update_page()
                return
        else:
            self._view.create_alert("Attenzione la matricola deve essere di tipo numerico!")

        self._view._txt_result.controls.append(ft.Text(f"La matricola {matricola} è stata iscritta correttamente al corso {codice}",
                                                       color="green"))
        self._view.update_page()