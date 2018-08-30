from tkinter import *



class Application(Frame):
    def __init__(self, master):
        super(Application,self).__init__(master)
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
        b1=Button(self, text = "Hello", command = self.hello).grid(row=0,column = 1, sticky="nesw")
        l1=Label(self,width=5).grid(row=0,column=0,columnspan=1,sticky="nesw")
        cb1=Checkbutton(self,text="Fullscreen",variable=fullscreen).grid(row=1,column=1)
        b2=Button(self,text="Done",command=self.done).grid(row=2,column=1,sticky="nesw")
        
    def hello(self):
        print("Hello")
    
    def done(self):
        print(fullscreen.get())

root=Tk()
fullscreen=IntVar()
root.title("Game Launcher")
root.minsize(600, 400)
app=Application(root)
root.mainloop()
