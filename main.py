import translator as tr

t = tr.Translator()
t.loadDictionary("dictionary.txt")
while(True):

    t.printMenu()
    scelta=input("Scelta: ")

    if scelta == '1':
        print("Inserisci parola aliena e traduzione")
        nuova_parola = input()
        entry=nuova_parola.split()
        if len (entry) == 2:
            t.handleAdd(entry)
    elif scelta == '2':
        query=input("Inserisci parola aliena: ")
        t.handleTranslate(query)
    if scelta == '3':
        pass
    if scelta == '4':
        break