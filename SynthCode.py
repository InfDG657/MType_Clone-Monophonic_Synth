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
        self.bindings()

    def widgets(self):
        self.keyboard = ttk.Label(self, image=self.keyboard_img)
        self.label1 = ttk.Label(self, text='A', font='fixedsys 24 bold')
        self.label2 = ttk.Label(self, text='S', font='fixedsys 24 bold')
        self.label3 = ttk.Label(self, text='D', font='fixedsys 24 bold')
        self.label4 = ttk.Label(self, text='F', font='fixedsys 24 bold')
        self.label5 = ttk.Label(self, text='G', font='fixedsys 24 bold')
        self.label6 = ttk.Label(self, text='H', font='fixedsys 24 bold')
        self.label7 = ttk.Label(self, text='J', font='fixedsys 24 bold')
        self.label8 = ttk.Label(self, text='K', font='fixedsys 24 bold')
        self.label9 = ttk.Label(self, text='W', font='fixedsys 24 bold', background='white', foreground='black')
        self.label10 = ttk.Label(self, text='E', font='fixedsys 24 bold', background='white', foreground='black')
        self.label11 = ttk.Label(self, text='T', font='fixedsys 24 bold', background='white', foreground='black')
        self.label12 = ttk.Label(self, text='Y', font='fixedsys 24 bold', background='white', foreground='black')
        self.label13 = ttk.Label(self, text='U', font='fixedsys 24 bold', background='white', foreground='black')

        self.original_bg = self.label1.cget('background')

        self.key_map = {
            'a': (self.label1, self.original_bg),
            's': (self.label2, self.original_bg),
            'd': (self.label3, self.original_bg),
            'f': (self.label4, self.original_bg),
            'g': (self.label5, self.original_bg),
            'h': (self.label6, self.original_bg),
            'j': (self.label7, self.original_bg),
            'k': (self.label8, self.original_bg),
            'w': (self.label9, 'white'),
            'e': (self.label10, 'white'),
            't': (self.label11, 'white'),
            'y': (self.label12, 'white'),
            'u': (self.label13, 'white')
        }
    def placement(self):
        self.keyboard.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.label1.place(relx=0.0625, rely=.75, anchor='center')
        self.label2.place(relx=0.1875, rely=.75, anchor='center')
        self.label3.place(relx=0.3125, rely=.75, anchor='center')
        self.label4.place(relx=0.4375, rely=.75, anchor='center')
        self.label5.place(relx=0.5625, rely=.75, anchor='center')
        self.label6.place(relx=0.6875, rely=.75, anchor='center')
        self.label7.place(relx=0.8125, rely=.75, anchor='center')
        self.label8.place(relx=0.9375, rely=.75, anchor='center')
        self.label9.place(relx=0.125, rely=.5, anchor='center')
        self.label10.place(relx=0.25, rely=.5, anchor='center')
        self.label11.place(relx=0.5, rely=.5, anchor='center')
        self.label12.place(relx=0.625, rely=.5, anchor='center')
        self.label13.place(relx=0.75, rely=.5, anchor='center')

    def bindings(self):
        for key in ['a', 'A']:
            self.master.bind(f'<KeyPress-{key}>', self.handle_key_press)
            self.master.bind(f'<KeyRelease-{key}>', self.handle_key_release)
        for key in ['s', 'S']:
            self.master.bind(f'<KeyPress-{key}>', self.handle_key_press)
            self.master.bind(f'<KeyRelease-{key}>', self.handle_key_release)
        for key in ['d', 'D']:
            self.master.bind(f'<KeyPress-{key}>', self.handle_key_press)
            self.master.bind(f'<KeyRelease-{key}>', self.handle_key_release)
        for key in ['f', 'F']:
            self.master.bind(f'<KeyPress-{key}>', self.handle_key_press)
            self.master.bind(f'<KeyRelease-{key}>', self.handle_key_release)
        for key in ['g', 'G']:
            self.master.bind(f'<KeyPress-{key}>', self.handle_key_press)
            self.master.bind(f'<KeyRelease-{key}>', self.handle_key_release)
        for key in ['h', 'H']:
            self.master.bind(f'<KeyPress-{key}>', self.handle_key_press)
            self.master.bind(f'<KeyRelease-{key}>', self.handle_key_release)
        for key in ['j', 'J']:
            self.master.bind(f'<KeyPress-{key}>', self.handle_key_press)
            self.master.bind(f'<KeyRelease-{key}>', self.handle_key_release)
        for key in ['k', 'K']:
            self.master.bind(f'<KeyPress-{key}>', self.handle_key_press)
            self.master.bind(f'<KeyRelease-{key}>', self.handle_key_release)
        for key in ['w', 'W']:
            self.master.bind(f'<KeyPress-{key}>', self.handle_key_press)
            self.master.bind(f'<KeyRelease-{key}>', self.handle_key_release)
        for key in ['e', 'E']:
            self.master.bind(f'<KeyPress-{key}>', self.handle_key_press)
            self.master.bind(f'<KeyRelease-{key}>', self.handle_key_release)
        for key in ['t', 'T']:
            self.master.bind(f'<KeyPress-{key}>', self.handle_key_press)
            self.master.bind(f'<KeyRelease-{key}>', self.handle_key_release)
        for key in ['y', 'Y']:
            self.master.bind(f'<KeyPress-{key}>', self.handle_key_press)
            self.master.bind(f'<KeyRelease-{key}>', self.handle_key_release)
        for key in ['u', 'U']:
            self.master.bind(f'<KeyPress-{key}>', self.handle_key_press)
            self.master.bind(f'<KeyRelease-{key}>', self.handle_key_release)

    def handle_key_press(self, event):
        key = event.char.lower()
        if key in self.key_map:
            label, original_bg = self.key_map[key]
            label.config(background='blue')

    def handle_key_release(self, event):
        key = event.char.lower()
        if key in self.key_map:
            label, original_bg = self.key_map[key]
            label.config(background=original_bg)

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