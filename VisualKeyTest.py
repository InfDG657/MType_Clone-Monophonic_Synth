import ttkbootstrap as ttk

root = ttk.Window(themename='vapor')

meter = ttk.Meter(amountused=1,  interactive = True, amounttotal=10)
meter.pack()

button = ttk.Button(text='Get Amount', command=lambda : print(meter.amountusedvar.get()) )
button.pack()

root.mainloop()
