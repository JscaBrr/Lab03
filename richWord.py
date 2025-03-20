#metodi gestione dati dizionario --> Model
class RichWord:
    def __init__(self, parola):
        self._parola = parola # this is a string
        self._esito = False #this is a bool

    @property
    def esito(self):
        # print("getter of parola called" )
        return self._esito

    @esito.setter
    def esito(self, boolValue):
        # print("setter of parola called" )
        self._esito = boolValue

    def __str__(self):
        return self._parola