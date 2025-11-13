import tkinter as tk
import ttkbootstrap as ttk
from PIL import Image, ImageTk

class KeyboardFrame(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent, width=1000, height=500)

        image_original = Image.open(r'Assets/piano.jpg').resize((1000,500))
        self.keyboard_img = ImageTk.PhotoImage(image_original)
        self.widgets()
        self.placement()

    def widgets(self):
        self.keyboard = ttk.Label(self, image=self.keyboard_img)
    def placement(self):
        self.keyboard.pack()

class MainWin(ttk.Window):
    def __init__(self):
        super().__init__(themename='cyborg')
        self.resizable(False, False)

        self.frames()
        self.placement()
        self.mainloop()

    def frames(self):
        self.keyboard = KeyboardFrame(self)
    
    def placement(self):
        self.keyboard.pack()

if __name__ == '__main__':
    window = MainWin()