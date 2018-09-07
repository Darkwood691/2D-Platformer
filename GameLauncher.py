from tkinter import *

class Application(Frame):
        
    
    def __init__(self, master):
        super(Application,self).__init__(master)
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
        l1=Label(self,width=4).grid(row=0,column=0,columnspan=1,sticky="nesw")
        l2=Label(self,text="")
        b1=Button(self, text = "Hello", command = self.hello).grid(row=1,column = 1, sticky="nesw")
        cb1=Checkbutton(self,text="Fullscreen",variable=fullScreen).grid(row=2,column=1)
        b2=Button(self,text="Done",command=self.done).grid(row=3,column=1,sticky="nesw")
        
        popupMenu = OptionMenu(self, menuVar,"one","two","three").grid(row=5,column=5,sticky="nesw")
                
    def hello(self):
        print("Hello")
    
    def done(self):
        print(fullScreen.get())

root=Tk()
fullScreen=IntVar()
menuVar=StringVar(root)
menuVar.set("one")
root.title("Game Launcher")
root.minsize(600, 400)
app=Application(root)


root.mainloop()
