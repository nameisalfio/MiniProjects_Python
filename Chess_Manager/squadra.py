from giocatore import Giocatore

class Squadra :

    def __init__(self, nome_squadra, giocatori):
       self.nome = nome_squadra
       self.giocatori = giocatori
       self.punteggio = 0
    
    def visualizza_informazioni_squadra(self):
        print(f"Nome squadra: {self.nome}")
        print(f"\nComponenti:\n")
        
        for giocatore in self.giocatori:
            print("--> ", end="")
            giocatore.visualizza_informazioni()
    