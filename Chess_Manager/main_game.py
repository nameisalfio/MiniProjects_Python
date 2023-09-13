from giocatore import Giocatore
from squadra import Squadra
import random
import time
import sys

def display(giocatori):
    i = 1
    for giocatore in giocatori:
        print(f"{i}. ", end="") # end="" impedisce il ritorno a capo
        giocatore.visualizza_informazioni()
        i = i+1

def mostra_menù():
    print("="*40)
    print("\t\tAZIONI\n")
    print("[1]\tSimula Turno\n")
    print("[2]\tSquadre\n")
    print("[3]\tClassifica\n")
    print("[4]\tEsci\n")
    print("="*40)

def simulazione_partita():
    print("Prima di iniziare, conosci già la modalità di gioco? \n")
    time.sleep(1)
    while True :
        scelta_utente = (input("1) Sì, ho già giocato altre volte\n2) No, è la prima volta che gioco\n\n"))

        if scelta_utente == "1":
            time.sleep(1)
            print("Perfetto, allora possiamo iniziare\n")
            break

        elif scelta_utente == "2":
            print("Non preoccuparti, ti spiegherò tutto quello che c'è da sapere\n")
            print("="*110)
            print("Il torneo si svolgerà nel seguente modo:\n\n\nOgni singolo giocatore si affronterà solo una volta contro un avversario, differente per ogni giocatore.\n\nPer ogni vittoria alla tua squadra verrà attribuito 1 punto, per ogni sconfitta 0 punti e per ogni pareggio entrambe le squadre guadagneranno 0,5 punti.\n\nLa squadra con il maggior numero di punti vincerà il torneo.\n\nIn caso di pareggio si effettuerà una sola partita fra i due giocatori con il punteggio Elo maggiore.\n\nInoltre ti consiglio di attenzionare i punteggi Elo di ogni tuo giocatore e degli avversari in modo tale da avere più probabilità di vincita\n")
            print("="*110)
            time.sleep(1) 
            print("Ora siamo pronti per iniziare\n" )
            break
        else:
            print("\nIl valore digitato non corrisponde con nessuna opzione disponibile, inserisci il numero 1 se sei già a conoscenza delle modalità di gioco o 2 se non le conosci\n")
            time.sleep(2)
            continue

    squadra_avversaria = squadra_avversaria1
    print("\nLa sala inizia a riempirsi...\n")
    time.sleep(1)
    print("Iniziano a posizionare le pedine nelle scacchiere\n")
    time.sleep(1)
    print("\nIn un tabellone vengono scritti le squadre gareggianti con i corrispettivi giocatori e punteggi Elo\n")
    time.sleep(1)

    print("\nVuoi vedere il tabellone?\n")
    while True:
        scelta = (input("1) Sì\n2) No, non mi interessa\n\n"))

        if scelta == "1":
            if random.randint(1,3) == 1:
                print(f"la squadra {squadra.nome} gareggerà contro la squadra {squadra_avversaria1.nome} e {squadra_avversaria2.nome} gareggerà contro {squadra_avversaria3.nome}\n")
                
            elif random.randint(1,3) == 2:
                print(f"la squadra {squadra.nome} gareggerà contro la squadra {squadra_avversaria2.nome} e {squadra_avversaria1.nome} gareggerà contro {squadra_avversaria3.nome}\n")
                squadra_avversaria = squadra_avversaria2

            elif random.randint(1,3) == 3:
                print(f"la squadra {squadra.nome} gareggerà contro la squadra {squadra_avversaria3.nome} e {squadra_avversaria2.nome} gareggerà contro {squadra_avversaria1.nome}\n")
                squadra_avversaria = squadra_avversaria2

            # Vengono ancora visualizzate le squadre    
                
            print(f"\n\nNome della squadra: {squadra.nome} \n")
            display(squadra.giocatori)

            print(f"\n\nNome della squadra: {squadra_avversaria1.nome} \n")
            display(squadra_avversaria1.giocatori)

            print(f"\n\nNome della squadra: {squadra_avversaria2.nome} \n")
            display(squadra_avversaria2.giocatori)

            print(f"\n\nNome della squadra: {squadra_avversaria3.nome} \n")
            display(squadra_avversaria3.giocatori)

            time.sleep(2)

            # --------------------------------------
            
            scelta2 = input("appena sei pronto inserisci 1\n\n1)Iniziamo\n")
            if scelta2 == "1":
                break
            else:
                print("Il valore digitato non corrisponde all'opzione disponibile, inserisci il numero 1 se sei pronto\n")
                continue
        elif scelta == "2":
            break

        else:
            print("Il valore digitato non corrisponde con nessuna opzione disponibile, inserisci il numero 1 se sei già a conoscenza delle modalità di gioco o 2 se non le conosci\n")
            continue
        break
        
    print("Ora siamo pronti per iniziare\n")
    print(f"Il tuo avversari '{squadra_avversaria.nome}' gareggeranno nel seguente ordine:\n ")
    display(squadra_avversaria.giocatori)

    print("\nScegli l'ordine in cui devono giocare i tuoi giocatori, il primo giocatore si sfiderà contro il primo avversario, il secondo con il secondo e il terzo con il terzo\n\n")
    
    ordine_squadra = []
    num_selezioni = 0
    while num_selezioni < len(squadra.giocatori):
        
        # Visualizzo i giocatori disponibili
        print("\nGiocatori disponibili: \n")
        display(lista_giocatori)
        scelta3 = input("-> Seleziona un giocatore (inserisci il numero corrispondente): \n")
        scelta3 = int(scelta3)

        if scelta3 < 1 or scelta3 > len(squadra.giocatori):
            print("Scelta non valida. Inserisci un numero valido.\n")
            continue

        tuo_giocatore_selezionato = squadra.giocatori.pop(scelta3-1)
        ordine_squadra.append(tuo_giocatore_selezionato)
        num_selezioni += 1
        print("seleziona il giocatore successivo per completare l'ordine della tua squadra\n")

    print("La tua squadra gareggerà nel seguente ordine:\n\n ")
    for idx, giocatore4 in enumerate(ordine_squadra, start=1):
        print(f"{idx}. {giocatore4.nome} {giocatore4.cognome} - Elo: {giocatore4.Elo}\n")
        
    return print("Inizia il torneo")

def determina_vincitore_tra_due(giocatore1, giocatore2, differenza_patta=50):
    numero_casuale_giocatore1 = random.randint(1, giocatore1.Elo)
    numero_casuale_giocatore2 = random.randint(1, giocatore2.Elo)

    differenza = abs(numero_casuale_giocatore1 - numero_casuale_giocatore2)

    if differenza < differenza_patta:
        risultato = "Pareggio"
    elif numero_casuale_giocatore1 > numero_casuale_giocatore2:
        risultato = giocatore1
    else:
        risultato = giocatore2

    return risultato

def determina_vincitore_tra_squadre(squadra1, squadra_avversaria1):
    vincitori_individuali = []
    #non so perchè ma non riesco a far funzionare questa parte
    for i in range(3):
        vincitore_giocatore = determina_vincitore_tra_due(squadra_avversaria1.giocatori[i], squadra1.giocatori[i], differenza_patta=30)
        vincitori_individuali.append(vincitore_giocatore)

    punteggio_squadra1 = sum(g.Elo for g in vincitori_individuali if g in squadra1.giocatori)
    punteggio_squadra2 = sum(g.Elo for g in vincitori_individuali if g in squadra_avversaria1.giocatori)

    if punteggio_squadra1 > punteggio_squadra2:
        return squadra1.nome
    elif punteggio_squadra2 > punteggio_squadra1:
        return squadra_avversaria1.nome
    else:
        return "Pareggio"






print("Benvenuto nel gioco di Chess Manager, sarai in grado di portare alla vittoria la tua squadra?\n")
time.sleep(2)
print("Dimenticavo, non hai ancora una squadra, cosa aspetti? Affrettati e crea la tua squadra nel miglior modo possibile\n")
time.sleep(2)
lista_giocatori = [Giocatore("Daniela", "Mangione", 1000),
                   Giocatore("Maria", "Nastro", 900),
                   Giocatore("Cristina","Mangione",1200),
                   Giocatore("Giorgio", "Moro",300),
                   Giocatore("Alessandro", "Mazza",790),
                   Giocatore("Sergio", "Pirrone",1300)]

lista_avversari1 = [Giocatore("Sergio", "Simoni", 1956),
                   Giocatore("Federico", "Corvi", 600),
                   Giocatore("Adriana","Carnicelli",444)]

lista_avversari2 = [Giocatore("Davide", "Olivetti", 1430),
                   Giocatore("Luca", "Brunello", 824),
                   Giocatore("Fernando","Stuzzi",715)]

lista_avversari3 = [Giocatore("Simone", "Godena", 563),
                   Giocatore("Seraphine", "Folco", 1253),
                   Giocatore("Carlo","Altini",915)]

nome_squadra_avversaria1 = "Cavalli Impavidi"
nome_squadra_avversaria2 = "Scacchi Sovrani"
nome_squadra_avversaria3 = "Pedoni Astuti"

squadra_avversaria1 = Squadra(nome_squadra_avversaria1,lista_avversari1)
squadra_avversaria2 = Squadra(nome_squadra_avversaria2,lista_avversari2)
squadra_avversaria3 = Squadra(nome_squadra_avversaria3,lista_avversari3)

limite_punteggio = 3000

# Creazione squadra
nome_squadra = input("\nInserisci il nome della tua squadra: ")
print("\nLa tua squadra sarà formata da 3 giocatori, il punteggio Elo della squadra non deve superare i 3000 punti Elo, scegli i tuoi giocatori con attenzione\n")
squadra = []

while len(squadra) < 3:

    # Visualizzo i giocatori disponibili
    print("\nGiocatori disponibili: \n")
    display(lista_giocatori)

    scelta = input("Seleziona un giocatore (inserisci il numero corrispondente): ")

    while not (scelta.isnumeric() and (int(scelta) >= 1 and int(scelta) <= len(lista_giocatori))):
        print("Il valora assegnato non corrisponde con quello dell'elenco, inserisci solo i valori disponibili\n")
        scelta = input("Seleziona un giocatore (inserisci il numero corrispondente): \n")

    scelta = int(scelta)
    giocatore_selezionato = lista_giocatori[scelta-1]
    print(f"\n --> Hai selezionato {giocatore_selezionato.nome} {giocatore_selezionato.cognome}\n")

    punteggio_totale = sum(giocatore.Elo for giocatore in squadra) 
    if sum(giocatore.Elo for giocatore in squadra) + giocatore_selezionato.Elo <= limite_punteggio:
        squadra.append(giocatore_selezionato)

    else:
        print(f"\nHai superato il valore limite dei punti Elo della tua squadra,puoi raggiungere un massimo di 3000 punti Elo. Il tuo punteggio è {punteggio_totale}, scegli un altro giocatore\n")
        time.sleep(3)
        continue
    
    lista_giocatori.remove(giocatore_selezionato)

squadra = Squadra(nome_squadra, squadra)

print("\n\nSquadra creata con successo! I giocatori selezionati sono: \n")
time.sleep(1)
display(squadra.giocatori)
time.sleep(1)

turno = 1
while turno < 6:

    print("="*40)
    print(f"{turno}° turno")
    mostra_menù()
    scelta = input("Seleziona un'opzione inserendo un numero: ")
    
    if scelta == "1":
        simulazione_partita()

    elif scelta == "2":

        print(f"\n\nNome della squadra: {squadra.nome} \n")
        display(squadra.giocatori)

        print(f"\n\nNome della squadra: {squadra_avversaria1.nome} \n")
        display(squadra_avversaria1.giocatori)

        print(f"\n\nNome della squadra: {squadra_avversaria2.nome} \n")
        display(squadra_avversaria2.giocatori)

        print(f"\n\nNome della squadra: {squadra_avversaria3.nome} \n")
        display(squadra_avversaria3.giocatori)

        time.sleep(2)

    elif scelta == "3":
        print("Ecco la classifica delle squadre: \n")
        for giocatore in lista_giocatori:
            giocatore.visualizza_informazioni()

    elif scelta == "4":
        print("Hai selezionato il numero 4, esci dal proramma")
        sys.exit(0) # Terminazione dell'applicativo

    else:
        print("scelta non valida, selezionare un opzione valida")

# Esegui le sfide tra le squadre
vincitore_squadre = determina_vincitore_tra_squadre(Squadra("Tua Squadra", lista_giocatori), squadra_avversaria1)
vincitore_finale = determina_vincitore_tra_squadre(vincitore_squadre, squadra_avversaria2)

# Stampa il risultato
if vincitore_finale == "Pareggio":
    print("La partita è finita in pareggio tra le squadre.")
else:
    print(f"La squadra vincitrice è {vincitore_finale}")

# Controlla se ci sono almeno due squadre con lo stesso punteggio Elo più alto
squadre = [Squadra("Tua Squadra", lista_giocatori), squadra_avversaria1, squadra_avversaria2, squadra_avversaria3]
squadre.sort(key=lambda squadra: sum(g.Elo for g in squadra.giocatori), reverse=True)

if squadre[0].nome == squadre[1].nome:
    print(f"Ulteriore sfida tra i due giocatori migliori di {squadre[0].nome} e {squadre[1].nome}")
    vincitore_sfida = determina_vincitore_tra_due(squadre[0].giocatori[0], squadre[1].giocatori[0], differenza_patta=30)
    if vincitore_sfida == "Pareggio":
        print("La sfida è finita in pareggio.")
    else:
        print(f"Il vincitore della sfida è {vincitore_sfida}")

# simulazione_partita:
    print('I vari giocatori si siedono nei rispettivi posti\n')
    print("3\n")
    print("2\n")
    print("1\n")
    print("Partono i timer\n")
    print("Spinta E3\n")
    print("Alfiere G5, con lo scopo di inchiodare il cavallo\n")
    print("Seguono mosse di svulippo dei pezzi\n")
    print("L'idea del bianco è di spingere il pedone per cacciare l'arfiere\n")
    print("Piccolo errore del bianco che passa in svantaggio\n ")
    print("Nero porta la regina in attacco\n")
    print("Il nero si prepara ad arroccare\n")
    print("Sacrificio di cavallo da parte del bianco\n")
    print("Scacco al re nero\n")