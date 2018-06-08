import sys

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
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'

        top.geometry("600x450+462+89")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")



        self.Button1 = Button(top)
        self.Button1.place(relx=0.68, rely=0.27, height=24, width=67)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Train''')
        self.Button1.configure(width=67)

        self.Entry1 = Entry(top)
        self.Entry1.place(relx=0.58, rely=0.11,height=20, relwidth=0.21)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(width=124)

        self.Entry2 = Entry(top)
        self.Entry2.place(relx=0.58, rely=0.18,height=20, relwidth=0.21)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(width=124)

        self.Label1 = Label(top)
        self.Label1.place(relx=0.42, rely=0.11, height=21, width=72)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''No of layers:''')

        self.Label2 = Label(top)
        self.Label2.place(relx=0.42, rely=0.18, height=21, width=91)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''No of iterations:''')

        self.Radiobutton1 = Radiobutton(top)
        self.Radiobutton1.place(relx=0.13, rely=0.11, relheight=0.06
                , relwidth=0.09)
        self.Radiobutton1.configure(activebackground="#d9d9d9")
        self.Radiobutton1.configure(activeforeground="#000000")
        self.Radiobutton1.configure(background="#d9d9d9")
        self.Radiobutton1.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1.configure(foreground="#000000")
        self.Radiobutton1.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1.configure(highlightcolor="black")
        self.Radiobutton1.configure(justify=LEFT)
        self.Radiobutton1.configure(text='''Flags''')

        self.Radiobutton2 = Radiobutton(top)
        self.Radiobutton2.place(relx=0.13, rely=0.18, relheight=0.06
                , relwidth=0.15)
        self.Radiobutton2.configure(activebackground="#d9d9d9")
        self.Radiobutton2.configure(activeforeground="#000000")
        self.Radiobutton2.configure(background="#d9d9d9")
        self.Radiobutton2.configure(disabledforeground="#a3a3a3")
        self.Radiobutton2.configure(foreground="#000000")
        self.Radiobutton2.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2.configure(highlightcolor="black")
        self.Radiobutton2.configure(justify=LEFT)
        self.Radiobutton2.configure(text='''Horse-colic''')

        self.Radiobutton3 = Radiobutton(top)
        self.Radiobutton3.place(relx=0.13, rely=0.24, relheight=0.06
                , relwidth=0.14)
        self.Radiobutton3.configure(activebackground="#d9d9d9")
        self.Radiobutton3.configure(activeforeground="#000000")
        self.Radiobutton3.configure(background="#d9d9d9")
        self.Radiobutton3.configure(disabledforeground="#a3a3a3")
        self.Radiobutton3.configure(foreground="#000000")
        self.Radiobutton3.configure(highlightbackground="#d9d9d9")
        self.Radiobutton3.configure(highlightcolor="black")
        self.Radiobutton3.configure(justify=LEFT)
        self.Radiobutton3.configure(text='''Ionosphere''')

        self.lab46 = Label(top)
        self.lab46.place(relx=0.1, rely=0.07, height=21, width=101)
        self.lab46.configure(background="#d9d9d9")
        self.lab46.configure(disabledforeground="#a3a3a3")
        self.lab46.configure(foreground="#000000")
        self.lab46.configure(text='''Select the dataset:''')

        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)



        self.Labelframe1 = LabelFrame(top)
        self.Labelframe1.place(relx=0.07, rely=0.4, relheight=0.57
                , relwidth=0.83)
        self.Labelframe1.configure(relief=GROOVE)
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(text='''Output:''')
        self.Labelframe1.configure(background="#d9d9d9")
        self.Labelframe1.configure(width=500)

        self.Canvas1 = Canvas(top)
        self.Canvas1.place(relx=0.08, rely=0.44, relheight=0.52, relwidth=0.81)
        self.Canvas1.configure(background="#d9d9d9")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief=RIDGE)
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="black")
        self.Canvas1.configure(width=483)






if __name__ == '__main__':
    vp_start_gui()
