import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self, text="Hello World\n(click me)", command = self.say_hi)
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",bg="yellow", command=root.destroy)
        self.quit.pack(side="bottom")
        #self.quit["bg"]="black"
    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()