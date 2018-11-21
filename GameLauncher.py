from tkinter import *

try:
    config = open("Settings.txt", "r")
    settings = config.read().split("z")
    print(settings)
    config.close()
    fail = False
except:
    fail = True

class Application(Frame):

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, width=2).grid(row=0, column=0, sticky="nesw")
        Label(self, width=10).grid(row=0, column=1, sticky="nesw")
        Label(self, width=14).grid(row=0, column=2, sticky="nesw")
        Label(self, text="Resolution:").grid(row=2, column=1)
        Label(self, text="Difficulty:").grid(row=4, column=1)
        Checkbutton(self, text="Fullscreen", variable=fullScreen).grid(row=3, column=2)
        resolutionMenu = OptionMenu(self, resolutionVar, "640x360", "864x486", "1280x720", "1366x768", "1920x1080")
        resolutionMenu.grid(row=2, column=2, sticky="nesw")
        OptionMenu(self, difficultyVar, "Easy", "Normal", "Hard").grid(row=4, column=2, sticky="nesw")
        Button(self, text="Done", command=self.exit).grid(row=5, column=2, sticky="nesw")

    def exit(self):
        config = open("Settings.txt", "w")

        res = str(resolutionVar.get())
        dif = str(difficultyVar.get())
        full = str(fullScreen.get())
        text = res + "z" + dif + "z" + full
        print(text)
        config.write(text)
        config.close()

        root.destroy()
        import MyGame

root = Tk()
fullScreen = IntVar()
resolutionVar = StringVar(root)
difficultyVar = StringVar(root)

if fail == False:
    resolutionVar.set(settings[0])
    difficultyVar.set(settings[1])
    fullScreen.set(settings[2])
elif fail == True:
    resolutionVar.set("1280x720")
    difficultyVar.set("Normal")
    fullScreen.set(0)

root.title("Game Launcher")
root.minsize(280, 180)
app = Application(root)
root.mainloop()

