"""
This is the GUI application for the pymaid tool.
This application will provide the user the following things:
1. A UI to compile  the .pmd files.
2. A pmd file editor (could be a live editor)
"""

# imports
import tkinter as tk
from tkinter import filedialog
import os


class MainFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.title('pymaid')

        self.bg_image = tk.PhotoImage(file = 'background.png')
        width, height = self.bg_image.width(), self.bg_image.height()

        self.background = tk.Canvas(self, height = height, width = width)
        self.background.pack()

        self.background.create_image(0, 0, image = self.bg_image, anchor = 'nw')

        compile_button = tk.Button(self.background, text = "Complie pmd", pady = 5,
                                   padx = 5, width = 15, relief = 'flat',
                                   bg = '#2abc8d', 
                                   activebackground = '#B39898')
        compile_button.place(x = 160, y = 190)

        editor_button = tk.Button(self.background, text = "Edit pmd", pady = 5,
                                   padx = 5, width = 15, relief = 'flat',
                                   bg = '#2abc8d', 
                                   activebackground = '#B39898')
        editor_button.place(x = 300, y = 190)

# main window
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('pym')
        self.geometry('610x400')
        self.resizable(False, False)
        self.icon = tk.PhotoImage(file = 'logo.png')
        self.iconphoto(False,self.icon)

        self.background = tk.Frame(self)
        self.background.pack(fill = 'both', expand = True)

        # self.frames[MainFrame.__name__] 
        frame = MainFrame(parent = self.background, controller = self)
        frame.grid(row = 0, column = 0, sticky = 'nesw')
        
    
if(__name__ == '__main__'):
    app = App()
    app.mainloop()