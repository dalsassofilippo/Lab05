class Studente:
    def __init__(self, matricola, cognome, nome, cds):
        self._matricola = matricola
        self._nome = cognome
        self._cognome = nome
        self._cds = cds

    def __str__(self):
        return f"{self._nome}, {self._cognome} ({self._matricola})"
