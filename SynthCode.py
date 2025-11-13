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
            self.master.bind(f'<KeyPress-{key}>', self.key_press_a)
            self.master.bind(f'<KeyRelease-{key}>', self.key_release_a)
        for key in ['s', 'S']:
            self.master.bind(f'<KeyPress-{key}>', self.key_press_s)
            self.master.bind(f'<KeyRelease-{key}>', self.key_release_s)
        for key in ['d', 'D']:
            self.master.bind(f'<KeyPress-{key}>', self.key_press_d)
            self.master.bind(f'<KeyRelease-{key}>', self.key_release_d)
        for key in ['f', 'F']:
            self.master.bind(f'<KeyPress-{key}>', self.key_press_f)
            self.master.bind(f'<KeyRelease-{key}>', self.key_release_f)
        for key in ['g', 'G']:
            self.master.bind(f'<KeyPress-{key}>', self.key_press_g)
            self.master.bind(f'<KeyRelease-{key}>', self.key_release_g)
        for key in ['h', 'H']:
            self.master.bind(f'<KeyPress-{key}>', self.key_press_h)
            self.master.bind(f'<KeyRelease-{key}>', self.key_release_h)
        for key in ['j', 'J']:
            self.master.bind(f'<KeyPress-{key}>', self.key_press_j)
            self.master.bind(f'<KeyRelease-{key}>', self.key_release_j)
        for key in ['k', 'K']:
            self.master.bind(f'<KeyPress-{key}>', self.key_press_k)
            self.master.bind(f'<KeyRelease-{key}>', self.key_release_k)
        for key in ['w', 'W']:
            self.master.bind(f'<KeyPress-{key}>', self.key_press_w)
            self.master.bind(f'<KeyRelease-{key}>', self.key_release_w)
        for key in ['e', 'E']:
            self.master.bind(f'<KeyPress-{key}>', self.key_press_e)
            self.master.bind(f'<KeyRelease-{key}>', self.key_release_e)
        for key in ['t', 'T']:
            self.master.bind(f'<KeyPress-{key}>', self.key_press_t)
            self.master.bind(f'<KeyRelease-{key}>', self.key_release_t)
        for key in ['y', 'Y']:
            self.master.bind(f'<KeyPress-{key}>', self.key_press_y)
            self.master.bind(f'<KeyRelease-{key}>', self.key_release_y)
        for key in ['u', 'U']:
            self.master.bind(f'<KeyPress-{key}>', self.key_press_u)
            self.master.bind(f'<KeyRelease-{key}>', self.key_release_u)

    def key_press_a(self, event):
        self.label1.config(background='blue')

    def key_release_a(self, event):
        self.label1.config(background=self.original_bg)

    def key_press_s(self, event):
        self.label2.config(background='blue')

    def key_release_s(self, event):
        self.label2.config(background=self.original_bg)

    def key_press_d(self, event):
        self.label3.config(background='blue')

    def key_release_d(self, event):
        self.label3.config(background=self.original_bg)

    def key_press_f(self, event):
        self.label4.config(background='blue')

    def key_release_f(self, event):
        self.label4.config(background=self.original_bg)

    def key_press_g(self, event):
        self.label5.config(background='blue')

    def key_release_g(self, event):
        self.label5.config(background=self.original_bg)

    def key_press_h(self, event):
        self.label6.config(background='blue')

    def key_release_h(self, event):
        self.label6.config(background=self.original_bg)

    def key_press_j(self, event):
        self.label7.config(background='blue')

    def key_release_j(self, event):
        self.label7.config(background=self.original_bg)

    def key_press_k(self, event):
        self.label8.config(background='blue')

    def key_release_k(self, event):
        self.label8.config(background=self.original_bg)

    def key_press_w(self, event):
        self.label9.config(background='blue')

    def key_release_w(self, event):
        self.label9.config(background='white')

    def key_press_e(self, event):
        self.label10.config(background='blue')

    def key_release_e(self, event):
        self.label10.config(background='white')

    def key_press_t(self, event):
        self.label11.config(background='blue')

    def key_release_t(self, event):
        self.label11.config(background='white')

    def key_press_y(self, event):
        self.label12.config(background='blue')

    def key_release_y(self, event):
        self.label12.config(background='white')

    def key_press_u(self, event):
        self.label13.config(background='blue')

    def key_release_u(self, event):
        self.label13.config(background='white')

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