#metodi gestione dati dizionario

class Dictionary:
    def __init__(self, lingua):
        self.lingua = lingua
        self.setdizionario = set()
        self._dict = {}
        self.loadDictionary(f"resources/{lingua}.txt")

    @property
    def dictdizionario(self):
        return self._dict #non è possibile accedere a _dict ma si accede a dictdizionario

    def __str__(self):
        print(self.setdizionario)

    def printAll(self):
        limit = 50
        if not self.setdizionario:
            print("ERRORE: Dizionario vuoto")
            return
        count = 0
        for i in self.setdizionario:
            print(i)
            count+=1
            if count >= limit:
                break

    def loadDictionary(self,filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                #self.setdizionario = set(line.strip().lower() for line in file)
                for line in file:
                    w = line.strip().lower()
                    self.setdizionario.add(w)
                    if w[0] in self.dictdizionario:
                        self.dictdizionario[w[0]].append(w)
                    else:
                        self.dictdizionario[w[0]] = [w]
        except FileNotFoundError:
            print(f"Errore: dizionario per {self.lingua} non trovato.")

