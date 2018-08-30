from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application,self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Button(self, text = "Hello", command = self.hello).grid(row=0,column = 1, sticky="nesw")
        Label(self,width=5).grid(row=0,column=0,columnspan=1,sticky="nesw")
    def hello(self):
        print("Hello")

root=Tk()
root.title("Game Launcher")
root.minsize(600, 400)
app=Application(root)
root.mainloop()
