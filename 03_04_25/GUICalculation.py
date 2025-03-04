from game import Game
from card import Card
import tkinter as tk

class MainWindow(tk.Frame):
    def __init__(self):
        super().__init__()
        
        self.setSize(800,600)
        self.master.title("Calculation")
        self.pack(fill="both", expand=True)
        self.gameArea = GameArea(self)
        
            #self.foundCards[i].grid(row=1, column=i, padx=5, pady=5)
        #self.master.rowconfigure(1, weight = 1)
        #self.master.columnconfigure(4, weight = 1)
        #self.grid(sticky = "nsew")
        
    def setSize(self, width, height):
        """Resets the window's width and height in pixels."""
        self.master.geometry(str(width)+ "x" + str(height))


class CardRender(tk.Canvas):
    def __init__(self, master, card:Card):
        super().__init__(master, width=100, height=150, borderwidth=0, relief="flat", highlightthickness=0,background="white")
        self.card = card
        
        self.draw()
        self.bind("<Button-1>", self.mouse_pressed)
        self.bind("<B1-Motion>", self.mouse_dragged)
        self.bind("<ButtonRelease-1>", self.mouse_released)

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

    def mouse_pressed(self, event):
        x = event.x_root - self.master.winfo_rootx()
        y = event.y_root - self.master.winfo_rooty()
        self.master.event_generate("<Button-1>", x=x, y=y)
    
    def mouse_dragged(self, event):
        x = event.x_root - self.master.winfo_rootx()
        y = event.y_root - self.master.winfo_rooty()
        self.master.event_generate("<B1-Motion>", x=x, y=y)

    def mouse_released(self,event):
        x = event.x_root - self.master.winfo_rootx()
        y = event.y_root - self.master.winfo_rooty()
        self.master.event_generate("<ButtonRelease-1>", x=x, y=y)

class GameArea(tk.Canvas):
    def __init__(self, master):
        super().__init__(master, background="green")
        self.pack(fill="both", expand=True)
        self.game = Game()
        self.foundation_pos = [{"x":150, "y":100},{"x":275, "y":100},{"x":400, "y":100},{"x":525, "y":100}]
        self.waste_pos = [{"x":100, "y":225},{"x":225, "y":225},{"x":350, "y":225},{"x":475, "y":225}]
        self.draw_pos = {"x0":400, "y0":425, "x1":500, "y1":575 }
        self.waste_rects = []
        self.drawn_card = None
        self.waste_num = -1
        self.selected_item = None
        self.waste_card = [0,0,0,0]
        for i in range(4):
            foundation = CardRender(self,self.game.foundations[i].cards[self.game.foundations[i].topCard])
            self.create_window(self.foundation_pos[i]["x"], self.foundation_pos[i]["y"], window=foundation)
            self.waste_rects.append(self.create_rectangle(self.waste_pos[i]["x"], self.waste_pos[i]["y"],self.waste_pos[i]["x"]+100, self.waste_pos[i]["y"]+150, fill="white", width=2))
        
        self.create_rectangle(self.draw_pos["x0"], self.draw_pos["y0"], self.draw_pos["x1"], self.draw_pos["y1"], fill="white", width=2)
        self.create_window(275,500, window=CardRender(self,None))
        self.draw_button = tk.Button(self.master, text="Draw Card", command=self.draw_card)
        self.create_window(150, 500, window=self.draw_button)
        self.bind("<Button-1>", self.mouse_pressed)
        self.bind("<B1-Motion>", self.mouse_dragged)
        self.bind("<ButtonRelease-1>", self.mouse_released)

    
    def draw_card(self):
        self.game.drawCard()
        self.drawn_card = CardRender(self, self.game.cardToPlay)
        self.drawn_card = self.create_window(450, 500, window=self.drawn_card)
        self.draw_button.configure(state="disabled")
        
    def mouse_pressed(self, event):
        self.x = event.x
        self.y = event.y
        self.selected_item = self.find_clicked_item(self.x, self.y)
        if self.selected_item == None and self.waste_num != -1:
            self.selected_item = self.waste_card[self.waste_num]
    def mouse_dragged(self, event):
        if self.selected_item:
             xDistance = event.x - self.x
             yDistance = event.y - self.y
             self.move(self.selected_item, xDistance, yDistance)
             self.x = event.x
             self.y = event.y
    
    def mouse_released(self, event):
        if self.selected_item == None:
            return
        foundationDrop = self.find_foundation(event.x, event.y)
        if foundationDrop != None:
            try:
                if self.waste_num != -1:
                    self.game.playCard(destNum=foundationDrop, source="waste", sourceNum=self.waste_num)
                    self.delete(self.waste_card[self.waste_num])
                    if self.game.wastes[self.waste_num].topCard != -1:
                        self.waste_card[self.waste_num] = self.create_window(self.waste_pos[self.waste_num]["x"] + 50, self.waste_pos[self.waste_num]["y"] + 75, window=CardRender(self, self.game.wastes[self.waste_num].cards[self.game.wastes[self.waste_num].topCard]))
                    else:
                        self.waste_card[self.waste_num] = 0
                    self.waste_num = -1

                else:

                    self.game.playCard(destNum=foundationDrop)
                    self.drawn_card = 0

                self.delete(self.selected_item)
                self.selected_item = None
                card = CardRender(self, self.game.foundations[foundationDrop].cards[self.game.foundations[foundationDrop].topCard])
                
                card1 = self.create_window(self.foundation_pos[foundationDrop]["x"], self.foundation_pos[foundationDrop]["y"], window=card)
                for i in range(4):
                    if self.waste_card[i] != 0:
                        self.delete(self.waste_card[i])
                        self.waste_card[i] = self.create_window(self.waste_pos[i]["x"] + 50, self.waste_pos[i]["y"] + 75, window=CardRender(self, self.game.wastes[i].cards[self.game.wastes[i].topCard]))
            except:
                 if self.waste_num != -1:
                     x = self.waste_pos[self.waste_num]["x"]+50 - self.coords(self.selected_item)[0]
                     y = self.waste_pos[self.waste_num]["y"] + 75 - self.coords(self.selected_item)[1]
                     self.move(self.selected_item, x,y)
                 else:
                     x = self.draw_pos["x0"] + 50 - self.coords(self.selected_item)[0] 
                     y = self.draw_pos["y0"] + 75 - self.coords(self.selected_item)[1] 
                     self.move(self.selected_item, x, y)

                 self.waste_num = -1
                 self.selected_item = None
        elif self.waste_num != -1:
            x = self.waste_pos[self.waste_num]["x"]+50 - self.coords(self.selected_item)[0]
            y = self.waste_pos[self.waste_num]["y"] + 75 - self.coords(self.selected_item)[1]
            self.move(self.selected_item, x, y)
        else:
             wasteDrop = self.find_waste(event.x, event.y)
             if wasteDrop != None:
                 self.game.playCard(destNum=wasteDrop, destination="waste", source="deck")
                 self.delete(self.selected_item)
                 self.selected_item = None
                 self.waste_card[wasteDrop] = self.create_window(self.waste_pos[wasteDrop]["x"] + 50, self.waste_pos[wasteDrop]["y"] + 75, window=CardRender(self, self.game.wastes[wasteDrop].cards[self.game.wastes[wasteDrop].topCard]))
                 self.drawn_card = 0
             else:
                 x = self.draw_pos["x0"] + 50 - self.coords(self.selected_item)[0] 
                 y = self.draw_pos["y0"] + 75 - self.coords(self.selected_item)[1] 
                 self.move(self.selected_item, x,y)
        if self.game.cardToPlay == None:
            self.draw_button.configure(state="normal")

    
    def find_clicked_item(self, x, y):
        if self.game.cardToPlay != None:
            coords = [self.draw_pos["x0"], self.draw_pos["y0"], self.draw_pos["x1"],self.draw_pos["y1"]]
            if self.contains_point(coords, x, y):
                return self.drawn_card
        for i in range(4):
            if self.game.wastes[i].topCard != -1:
                #topCard = self.game.wastes[i].getTopCard()
                coords = self.coords(self.waste_rects[i])
                if self.contains_point(coords, x, y):
                    self.waste_num = i
                    return None
        self.waste_num = -1
        return None
    
    def contains_point(self, coords, x, y):
        [x0, y0, x1, y1] = coords
        print(x,y, x0,y0, x1,y1)
        return x >= min(x0,x1) and x <= max(x0,x1) and y >= min(y0, y1) and y <= max(y0, y1)
    
    def find_foundation(self, x, y):
        for i in range(4):
            #topCard = foundation.getTopCard()
            coords = list(self.foundation_pos[i].values())
            coords[0] = coords[0]-50
            coords[1] = coords[1]-75
            coords.append(coords[0]+100)
            coords.append(coords[1]+
            150)
            #foundation.playCard(topCard)
            if self.contains_point(coords, x, y):
                return i
        return None
    def find_waste(self, x, y):
        for i in range(4):
            
            coords = self.coords(self.waste_rects[i])
            if self.contains_point(coords, x, y):
                
                return i
        return None

if __name__ == "__main__":
    game = Game()
    MainWindow().mainloop()