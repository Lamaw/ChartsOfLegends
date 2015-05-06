__author__ = 'antoine'

import Tkinter as tk
import ttk


class main_frame(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.__build_notebook()

    def __build_notebook(self, *args):
        self.notebook = ttk.Notebook()
        for arg in args:
            self.__add_notebook(arg)

    def __add_notebook(self, tab):

        widget = self.__build_widget(tab)
        self.notebook.add(widget)

    # Must parametrize the elements present in the tab, and associate the parameter with the "tab" name
    def __build_widget(self, tab_name):
        widget = tk.Frame()

        widget = __specify_widget(widget, tab_name)

        return widget



# ------------- STATIC METHODS ---------

def __specify_widget(widget, tab_name):

    if tab_name == "Hero_Zoom":
        pass