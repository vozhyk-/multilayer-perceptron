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


import random

import reading
import evaluation



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



        start_button = Button(top)
        start_button.place(relx=0.68, rely=0.27, height=24, width=67)
        start_button.configure(pady="0")
        start_button.configure(text='''Start''')
        start_button.configure(width=67)
        start_button.configure(command=self.train_and_evaluate)

        num_l1_neurons_entry = Entry(top)
        num_l1_neurons_entry.place(relx=0.58, rely=0.11,height=20, relwidth=0.10)
        num_l1_neurons_entry.configure(width=124)

        num_l2_neurons_entry = Entry(top)
        num_l2_neurons_entry.place(relx=0.68, rely=0.11,height=20, relwidth=0.10)
        num_l2_neurons_entry.configure(width=124)

        self.num_neurons = [StringVar(), StringVar()]
        self.num_neurons[0].set("16")
        self.num_neurons[1].set("16")

        num_l1_neurons_entry.configure(textvariable=self.num_neurons[0])
        num_l2_neurons_entry.configure(textvariable=self.num_neurons[1])

        max_training_error_entry = Entry(top)
        max_training_error_entry.place(relx=0.58, rely=0.18,height=20, relwidth=0.21)
        max_training_error_entry.configure(width=124)

        self.max_training_error = StringVar()
        self.max_training_error.set("0.8")
        max_training_error_entry.configure(textvariable=self.max_training_error)

        self.Label1 = Label(top)
        self.Label1.place(relx=0.42, rely=0.11, height=21)
        self.Label1.configure(text='''Number of neurons:''')

        self.Label2 = Label(top)
        self.Label2.place(relx=0.42, rely=0.18, height=21)
        self.Label2.configure(text='''Maximum training error:''')

        flags_radiobutton = Radiobutton(top)
        flags_radiobutton.place(relx=0.13, rely=0.11, relheight=0.06
                , relwidth=0.09)
        flags_radiobutton.configure(justify=LEFT)
        flags_radiobutton.configure(takefocus="0")
        flags_radiobutton.configure(text='''Flags''')

        horse_colic_radiobutton = Radiobutton(top)
        horse_colic_radiobutton.place(relx=0.13, rely=0.18, relheight=0.06
                , relwidth=0.15)
        horse_colic_radiobutton.configure(justify=LEFT)
        horse_colic_radiobutton.configure(takefocus="0")
        horse_colic_radiobutton.configure(text='''Horsecolic''')

        ionosphere_radiobutton = Radiobutton(top)
        ionosphere_radiobutton.place(relx=0.13, rely=0.24, relheight=0.06
                , relwidth=0.14)
        ionosphere_radiobutton.configure(justify=LEFT)
        ionosphere_radiobutton.configure(takefocus="0")
        ionosphere_radiobutton.configure(text='''Ionosphere''')

        self.dataset_choice = IntVar()
        self.dataset_choice.set(0)
        flags_radiobutton.configure(variable=self.dataset_choice, value=0)
        horse_colic_radiobutton.configure(variable=self.dataset_choice, value=1)
        ionosphere_radiobutton.configure(variable=self.dataset_choice, value=2)

        self.lab46 = Label(top)
        self.lab46.place(relx=0.1, rely=0.07, height=21)
        self.lab46.configure(text='''Select the dataset:''')


        self.output_frame = LabelFrame(top)
        self.output_frame.place(relx=0.07, rely=0.4, relheight=0.57
                , relwidth=0.83)
        self.output_frame.configure(relief=GROOVE)
        self.output_frame.configure(text='''Output:''')
        self.output_frame.configure(width=500)

    def train_and_evaluate(self):
        max_error = float(self.max_training_error.get())
        inner_layer_sizes = map(int,
            filter(lambda x: x != "",
                map(lambda var: var.get(),
                    self.num_neurons)))

        rows = reading.read_flag_dataset()

        random.shuffle(rows)
        training_set, test_set = evaluation.split_dataset(rows)

        network, training_errors = evaluation.trained_network(
            training_set, inner_layer_sizes, max_error=max_error)
        # TODO Show training_errors
        error = evaluation.evaluate_network(network, test_set)
        # TODO Show error

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

        canvas = FigureCanvasTkAgg(fig, master=self.output_frame)
        canvas.get_tk_widget().pack()
        canvas.draw()

if __name__ == '__main__':
    vp_start_gui()
