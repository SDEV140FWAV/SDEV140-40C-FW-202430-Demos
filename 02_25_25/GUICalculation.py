from game import Game
from card import Card
import tkinter as tk

class MainWindow(tk.Frame):
    def __init__(self):
        super().__init__()
        self.setSize(800,600)
        self.master.title("Calculation")
        self.card = Card("HEARTS", "A")
        self.card_render = CardRender(self,self.card)
        self.pack()
        self.card_render.pack()
    def setSize(self, width, height):
        """Resets the window's width and height in pixels."""
        self.master.geometry(str(width)+ "x" + str(height))


class CardRender(tk.Canvas):
    def __init__(self, master, card:Card):
        super().__init__(master, width=100, height=150, borderwidth=0, relief="flat", highlightthickness=0,background="white")
        self.card = card
        self.pack()
        self.draw()

    def draw(self):
        if self.card == None:
            for i in range(0,151,12):
                for j in range(0,101,12):
                    self.create_bitmap(j,i, bitmap="gray12", foreground="red")
        else:
            if self.card.suit == "DIAMONDS" or self.card.suit == "HEARTS":
                color = "red"
            else:
                color = "black"
            self.create_text(20, 25, text=f"{self.card.rank}", fill=color, font=("courier", 18))
            self.create_text(50, 75, text=Card.SUIT_SYMBOL[self.card.suit], fill=color, font=("courier",48))
            self.create_text(80, 125, text=f"{self.card.rank}",fill=color, font=("courier", 18))


if __name__ == "__main__":
    MainWindow().mainloop()