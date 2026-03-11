class Dictionary:
    def __init__(self):
        self.diz={}
        #file=open("dictionary.txt", "r")
        #for riga in file:
            #dati = riga.strip().split(" ")
            #aliena=dati[0]
            #traduzione=dati[1]
            #self.diz[aliena.lower()]=traduzione.lower()
        #file.close()

    def addWord(self, entry):
        aliena = entry[0].lower()
        traduzione = entry[1].lower()
        if aliena.isalpha() and traduzione.isalpha():
            self.diz[aliena]=traduzione
            return True
        else:
            return False

    def translate(self, parola):
        parola=parola.lower()
        if parola in self.diz:
            return self.diz[parola]
        else:
            return None


    def translateWordWildCard(self):
        pass