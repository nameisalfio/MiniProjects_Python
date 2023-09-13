from giocatore import Giocatore

class Squadra :

    def __init__(self, nome_squadra, giocatori: list[Giocatore]):
       self.nome = nome_squadra
       self.giocatori = giocatori
    
    def visualizza_informazioni_squadra(self):
        print(f"Nome squadra: {self.nome}")
        print(f"\nComponenti:\n")
        
        for giocatore in self.giocatori:
            print("--> ", end="")
            giocatore.visualizza_informazioni()
    