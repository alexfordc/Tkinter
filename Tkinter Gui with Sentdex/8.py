import tkinter as tk
from tkinter import ttk
import matplotlib
matplotlib.use("TkAgg") # change the backend

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

import numpy as np
import pandas as pd
import urllib
import json



LARGE_FONT = ('Verdana', 12)
style.use('ggplot')

f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)


def animate(i): # i for interval
    pullData = open('sampleData.txt', 'r').read()
    dataList = pullData.split('\n')
    xList = []
    yList = []
 
    for eachLine in dataList:
        if len(eachLine) > 1:
            x, y = eachLine.split(',')
            xList.append(int(x))
            yList.append(int(y))
    a.clear()
    a.plot(xList, yList)


class SeaofBTCapp(tk.Tk):
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs) # arguments and keyword arguments

        tk.Tk.iconbitmap(self, default="KawsMiffy.ico")
        tk.Tk.wm_title(self, "Sea of BTC client")



        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, BTCe_Page):
            
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")
            self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

def qf(var):
    print(var)

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="""ALPHA Bitcoin trading application, 
        use at your own risk. There is no promise of warranty""", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Agree", command=lambda :controller.show_frame(BTCe_Page))
        button1.pack()

        button2 = ttk.Button(self, text="Disagree", command=quit)
        button2.pack()





class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = ttk.Label(self, text="PageOne", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        button1 = ttk.Button(self, text="Back to Home", command=lambda :controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="PageTwo", command=lambda :controller.show_frame(PageTwo))
        button2.pack()


# class PageTwo(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)   
#         # super().__init__(parent) can also do, this is to call the parent tk.Frame __init__ method in order to use its variable
#         label = tk.Label(self, text="PageTwo", font=LARGE_FONT)
#         label.pack(pady=10, padx=10)
        
#         button1 = ttk.Button(self, text="Back to Home", command=lambda :controller.show_frame(StartPage))
#         button1.pack()

#         button2 = ttk.Button(self, text="Page One", command=lambda :controller.show_frame(PageOne))
#         button2.pack()


class BTCe_Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)   
        label = tk.Label(self, text="Graph Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        button1 = ttk.Button(self, text="Back to Home", command=lambda :controller.show_frame(StartPage))
        button1.pack()

        

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack()

app = SeaofBTCapp()
ani = animation.FuncAnimation(f, animate, interval=1000)
app.mainloop()













# print(help(SeaofBTCapp))
# print(help(StartPage))
    






