class Corso:

    def __init__(self,codice,crediti,nome,pd):
        self._codice=codice
        self._crediti=crediti
        self._nome=nome
        self._pd=pd

    def __str__(self):
        return f"{self._nome} ({self._codice})"