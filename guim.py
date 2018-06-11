import sys
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True



def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel (root)
    root.mainloop()

w = None
def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel (w)
    _support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel():
    global w
    w.destroy()
    w = None


class New_Toplevel:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        top.geometry("600x450+462+89")
        top.title("MLP Project")



        self.Button1 = Button(top)
        self.Button1.place(relx=0.68, rely=0.27, height=24, width=67)
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Train''')
        self.Button1.configure(width=67)

        self.Button3 = Button(top)
        self.Button3.place(relx=0.32, rely=0.27, height=24, width=37)
        self.Button3.configure(takefocus="0")
        self.Button3.configure(text='''Load''')

        self.Button4 = Button(top)
        self.Button4.place(relx=0.6, rely=0.27, height=24, width=32)
        self.Button4.configure(takefocus="0")
        self.Button4.configure(text='''Plot''')

        self.Entry1 = Entry(top)
        self.Entry1.place(relx=0.58, rely=0.11,height=20, relwidth=0.21)
        self.Entry1.configure(width=124)

        self.Entry2 = Entry(top)
        self.Entry2.place(relx=0.58, rely=0.18,height=20, relwidth=0.21)
        self.Entry2.configure(width=124)

        self.Label1 = Label(top)
        self.Label1.place(relx=0.42, rely=0.11, height=21, width=72)
        self.Label1.configure(text='''No of layers:''')

        self.Label2 = Label(top)
        self.Label2.place(relx=0.42, rely=0.18, height=21, width=91)
        self.Label2.configure(text='''No of iterations:''')

        self.Radiobutton1 = Radiobutton(top)
        self.Radiobutton1.place(relx=0.13, rely=0.11, relheight=0.06
                , relwidth=0.09)
        self.Radiobutton1.configure(justify=LEFT)
        self.Radiobutton1.configure(takefocus="0")
        self.Radiobutton1.configure(text='''Flags''')

        self.Radiobutton2 = Radiobutton(top)
        self.Radiobutton2.place(relx=0.13, rely=0.18, relheight=0.06
                , relwidth=0.15)
        self.Radiobutton2.configure(justify=LEFT)
        self.Radiobutton2.configure(takefocus="0")
        self.Radiobutton2.configure(text='''Horse-colic''')

        self.Radiobutton3 = Radiobutton(top)
        self.Radiobutton3.place(relx=0.13, rely=0.24, relheight=0.06
                , relwidth=0.14)
        self.Radiobutton3.configure(justify=LEFT)
        self.Radiobutton3.configure(takefocus="0")
        self.Radiobutton3.configure(text='''Ionosphere''')

        self.lab46 = Label(top)
        self.lab46.place(relx=0.1, rely=0.07, height=21, width=101)
        self.lab46.configure(text='''Select the dataset:''')


        self.Labelframe1 = LabelFrame(top)
        self.Labelframe1.place(relx=0.07, rely=0.4, relheight=0.57
                , relwidth=0.83)
        self.Labelframe1.configure(relief=GROOVE)
        self.Labelframe1.configure(text='''Output:''')
        self.Labelframe1.configure(width=500)



class mclass:
    def __init__(self,  window):
        self.window = window
        self.box = Entry(window)
        self.button = Button (window, text="check", command=self.plot)
        self.box.pack ()
        self.button.pack()

    def plot (self):
        x=np.array ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        v= np.array ([16,16.31925,17.6394,16.003,17.2861,17.3131,19.1259,18.9694,22.0003,22.81226])
        p= np.array ([16.23697,     17.31653,     17.22094,     17.68631,     17.73641 ,    18.6368,
            19.32125,     19.31756 ,    21.20247  ,   22.41444   ,  22.11718  ,   22.12453])

        fig = Figure(figsize=(6,6))
        a = fig.add_subplot(111)
        a.scatter(v,x,color='red')
        a.plot(p, range(2 +max(x)),color='blue')
        a.invert_yaxis()

        a.set_title ("Estimation Grid", fontsize=16)
        a.set_ylabel("Y", fontsize=14)
        a.set_xlabel("X", fontsize=14)

        canvas = FigureCanvasTkAgg(fig, master=self.window)
        canvas.get_tk_widget().pack()
        canvas.draw()

if __name__ == '__main__':
    vp_start_gui()
