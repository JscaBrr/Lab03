#metodi di logica algoritmo di base
import string
from multiDictionary import multiDictionary

class SpellChecker:

    def __init__(self):
        self.dizionario = None

    def handleSentence(self, txtIn):
        listatxt = self.replaceChars(txtIn)
        m = multiDictionary()
        m.dizionario = self.dizionario
        print(f"-----------metodo Countain-----------")
        errors = m.searchWord(listatxt)
        if errors:
            print(f"Parole errate trovate: \n{"\n".join(errors)}")
        else:
            print("Tutte le parole sono corrette.")
        print(f"-----------metodo Linear-----------")
        errors = m.searchWordLinear(listatxt)
        if errors:
            print(f"Parole errate trovate: \n{"\n".join(errors)}")
        else:
            print("Tutte le parole sono corrette.")
        print(f"-----------metodo Dicotomic-----------")
        errors = m.searchWordDichotomic(listatxt)
        if errors:
            print(f"Parole errate trovate: \n{"\n".join(errors)}")
        else:
            print("Tutte le parole sono corrette.")

    def replaceChars(self, testo):
        testo = testo.lower()
        testo = testo.translate(str.maketrans("", "", string.punctuation)).strip()
        listatesto = testo.split(" ")
        return listatesto
