import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Welcome to:\n The Still Unnamed Project\nVersion: 0.0.1')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 40, window=label1)

label2 = tk.Label(root, text='Type the Measurement ID\nof RIPE Atlas Traceroute:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)

def getSquareRoot ():
    
    x1 = entry1.get()
    

    
button1 = tk.Button(text='Generate graph', command=getSquareRoot, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)

root.mainloop()