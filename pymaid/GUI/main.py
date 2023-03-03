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

class Interface(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.bg_image = tk.PhotoImage(file = 'background.png')
        height, width = self.bg_image.height(), self.bg_image.width()

        self.background =  tk.Canvas(self, height = height, width = width)
        self.background.pack(fill = 'both', expand = True)

        self.background.create_image(0, 0, image = self.bg_image, anchor = 'nw')
        

class EditorFrame(Interface):
    def __init__(self, parent, controller):
        Interface.__init__(self, parent, controller)

        self.textbox = tk.Text(self, width = 50, height = 8, background='#ffffff',
                               insertbackground='Black')
        self.textbox.place(x = 90,y = 178)
        
        self.frame = tk.Frame(self, bg = '#B39898', width = 410, height = 150)
        self.frame.place(x = 100,y = 330)

        self.compile = tk.Button(self.frame, text = 'Compile', pady = 5,
                                   padx = 5, width = 10, relief = 'flat',
                                   bg = '#2abc8d', fg = '#000000',
                                   activebackground = '#B39898')
        self.compile.grid(row = 1, column = 0, pady = 5, padx = 5)

        self.status = tk.Label(self.frame, text = '--No Process--', pady = 5,
                               bg = "#ee3456", width = 20)
        self.status.grid(row = 1, column = 1, pady = 5, padx = 5)
        
        self.show = tk.Button(self.frame, text = 'Show', pady = 5, padx = 5,
                              width = 10,
                              relief = 'flat', bg = '#2abc8d', fg = '#000000',
                              activebackground = '#B39898', state = tk.DISABLED)
        self.show.grid(row = 1, column = 2, pady = 5, padx = 5)

        self.home = tk.Button(self, text = 'Home', pady = 5, padx = 5,
                              width = 10,
                              relief = 'flat', bg = '#2abc8d', fg = '#000000',
                              activebackground = '#B39898',
                              command = lambda: self.controller.show_frame('MainFrame'))
        self.home.place(x = 500, y = 178)

class CompileFrame(Interface):
    def __init__(self, parent, controller):
        Interface.__init__(self, parent, controller)
        
        self.frame = tk.Frame(self, bg = '#2AA2BC',width = 300, height = 150,
                              pady = 8, padx = 5)
        self.frame.place(x = 155, y = 190)

        self.file_label = tk.Label(self.frame, text = '---No Selection---',
                                   bg = '#ee3456', width = 25, pady = 5)
        self.file_label.grid(row = 1, column = 0, padx = 5, pady = 5)     
        self.select = tk.Button(self.frame, text = 'Select', pady = 5,
                                   padx = 5, width = 10, relief = 'flat',
                                   bg = '#2abc8d', fg = '#000000',
                                   activebackground = '#B39898',
                                   command = self.browse) 
        self.select.grid(row = 1, column = 1, padx = 5, pady = 5)

        self.compile = tk.Button(self.frame, text = 'Compile', pady = 5,
                                   padx = 5, width = 15, relief = 'flat',
                                   bg = '#2abc8d', fg = '#000000',
                                   activebackground = '#B39898')
        self.compile.grid(row = 2, column = 0, columnspan = 2, pady = 5)

        self.status = tk.Label(self.frame, text = '--No Process--', pady = 5,
                               bg = "#ee3456", width = 25)
        self.status.grid(row = 3, column = 0, padx = 5, pady = 5)
        
        self.show = tk.Button(self.frame, text = 'Show', pady = 5, padx = 5,
                              width = 10,
                              relief = 'flat', bg = '#2abc8d', fg = '#000000',
                              activebackground = '#B39898', state = tk.DISABLED)
        self.show.grid(row = 3, column = 1, padx = 5, pady = 5)

        self.home = tk.Button(self, text = 'Home', pady = 5, padx = 5,
                              width = 10,
                              relief = 'flat', bg = '#2abc8d', fg = '#000000',
                              activebackground = '#B39898',
                              command = lambda: self.controller.show_frame('MainFrame'))
        self.home.place(x = 500, y = 190)

    def browse(self):
        self.filename = filedialog.askopenfilename()
        if(self.filename):
            self.file_label.config(text = os.path.basename(self.filename))
        else:
            self.file_label.config(text = '---No Selection---')



class MainFrame(Interface):
    def __init__(self, parent, controller):
        Interface.__init__(self, parent, controller)

        compile_button = tk.Button(self.background, text = "Complie pmd", pady = 5,
                                   padx = 5, width = 15, relief = 'flat',
                                   bg = '#2abc8d', fg = '#000000',
                                   activebackground = '#B39898',
                                   command = lambda: self.controller.show_frame('CompileFrame'))
        compile_button.place(x = 160, y = 190)

        editor_button = tk.Button(self.background, text = "Edit pmd", pady = 5,
                                   padx = 5, width = 15, relief = 'flat',
                                   bg = '#2abc8d', fg = "#000000",
                                   activebackground = '#B39898',
                                   command = lambda: self.controller.show_frame('EditorFrame'))
        editor_button.place(x = 300, y = 190)

# main window
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('pymaid')
        self.geometry('610x400')
        self.resizable(False, False)
        self.icon = tk.PhotoImage(file = 'logo.png')
        self.iconphoto(False,self.icon)
        self.frames = {}

        self.background = tk.Frame(self)
        self.background.pack(fill = 'both', expand = True)

        # self.frames[MainFrame.__name__]
        for f in (EditorFrame,CompileFrame,MainFrame):
            frame = f(parent = self.background, controller = self)
            self.frames[f.__name__] = frame
            frame.grid(row = 0, column = 0, sticky = 'nesw')

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()
        
    
if(__name__ == '__main__'):
    app = App()
    app.mainloop()