#!/usr/bin/env/ python
import Tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit',
            command = self.quit)
        self.quitButton.grid()
        self.testButton = tk.Button(self, bitmap='error',
            command = print "Test")
        self.testButton.grid()

app = Application()
app.master.title('Sample application')
app.mainloop()
