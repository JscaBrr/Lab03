import correttore
from dictionary import Dictionary

while(True):
    print("______________________________\n" +
          "      SpellChecker 101\n" +
          "______________________________\n " +
          "Seleziona la lingua desiderata\n"
          "1. Italiano\n" +
          "2. Inglese\n" +
          "3. Spagnolo\n" +
          "4. Exit\n" +
          "______________________________\n")
    linguamain = int(input())
    if linguamain == 1:
        lingua = "Italian"
    elif linguamain == 2:
        lingua = "English"
    elif linguamain == 3:
        lingua = "Spanish"
    else:
        print("Programma terminato")
        break
    sc = correttore.SpellChecker()
    d = Dictionary(lingua)
    sc.dizionario = d
    txtIn = input(f"Inserisci la tua frase in {lingua}\n")
    sc.handleSentence(txtIn)


