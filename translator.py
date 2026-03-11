from dictionary import Dictionary

class Translator:

    def __init__(self):
        self.dictionary = Dictionary()

    def printMenu(self):
        print("-"*30)
        print("Translator Alien-Italian")
        print("-" * 30)
        print("1. Aggiungi nuova parola")
        print("2. Cerca una traduzione")
        print("3. Cerca con wildcard")
        print("4.  Stampa tutto il dizionario")
        print("5. Exit")
        print("-" * 30)

    def loadDictionary(self, dict_file):
        file=open(dict_file, "r")
        for riga in file:
            dati=riga.strip().split()
            if len(dati)==2:
                self.dictionary.addWord((dati[0],dati[1]))
        file.close()
        print("Dizionario modificato con successo!")

    def handleAdd(self, entry):
        if len(entry) == 2:
            successo=self.dictionary.addWord(entry)
            if successo:
                print ("Parola aggiunta correttamente")
            else:
                print("errore! sono ammesse solo lettere")
        else:
            print("errore di formato")


    def handleTranslate(self, query):
        traduzione=self.dictionary.translate(query)
        if traduzione is not None:
            print("Traduzione: ", traduzione)
        else:
            print("Parola non trovata")
    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        pass