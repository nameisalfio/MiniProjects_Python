class Giocatore:
    #definisco l'attributo di Giocatori
    def __init__(self, nome , cognome, Elo):
        self.nome = nome
        self.cognome = cognome
        self.Elo = Elo 
        
    # definisco il metodo dei giocatori
    def visualizza_informazioni(self):
        print(f"{self.nome} {self.cognome} - Elo: {self.Elo}\n")
