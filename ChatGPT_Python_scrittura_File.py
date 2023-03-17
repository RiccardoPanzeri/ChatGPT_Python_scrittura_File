#importo la libreria openai
import openai
#affinchè il programma funzioni, è necessario inserire qui la chiave API OpenAi personale.
openai.api_key = "Inserisci la tua chiave API OpenAI personale qui"
#creiamo le variabili necessarie, che contengono: 
#il modello dell'engine di completamento automatico di OpenAI
modelloEngine = "text-davinci-003"
restart = True;
domanda = input("Chiedi qualcosa all'AI: ")
while(restart == True):#mi assicuro che l'utente possa fare più di una domanda
#e l'input che verrà inserito dall'utente per interagire con l'AI
#con questa porzione di codice, andiamo a generare una risposta all'input, aggiustando i parametri di comportamento del bot: 
    completion = openai.Completion.create(
        engine = modelloEngine,
        prompt = domanda,
        max_tokens = 1024,
        n= 1,
        stop = None,
        temperature = 0.5,#la temperatura influisce sulla coerenza della risposta: più è alta, più varia ma meno accurata sarà la risposta all'input.
    )


    risposta = completion.choices[0].text #inseriamo la risposta generata in una variabile;

    #apro file in scrittura;
    file = open(r"testo.txt", "w")
    file.write(risposta)#scrivo la risposta sul file
    file.close()#chiudo il file

    print(risposta)#stampo la risposta dell'AI a schermo
    print("\n")
    domanda = input()

    







