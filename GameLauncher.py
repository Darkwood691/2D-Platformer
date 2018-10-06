from tkinter import *

#remap controlls

global fail
try:
    config=open("Settings.txt","r")
    settings=config.read().split("z")
    print(settings)
    config.close()
    fail=False
except:
    fail=True
    

class Application(Frame):
    
    def __init__(self, master):
        super(Application,self).__init__(master)
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
        l1=Label(self,width=2).grid(row=0,column=0,sticky="nesw")
        l2=Label(self,width=10).grid(row=0,column=1,sticky="nesw")
        l3=Label(self,width=14).grid(row=0,column=2,sticky="nesw")
        l4=Label(self,text="Resolution:").grid(row=2,column=1)
        l5=Label(self,text="Difficulty:").grid(row=4,column=1)
        #b1=Button(self, text = "Get Dropdown", command = self.dropdown).grid(row=1,column = 1, sticky="nesw")
        cb1=Checkbutton(self,text="Fullscreen",variable=fullScreen).grid(row=3,column=2)
        #cb2=Checkbutton(self,text="Do not show again",variable=showAgain).grid(row=7,column=2)
        #b2=Button(self,text="Check",command=self.done).grid(row=3,column=1,sticky="nesw")
        
        resolutionMenu=OptionMenu(self, resolutionVar,"640x360","864x486","1280x720","1366x768","1920x1080").grid(row=2,column=2,sticky="nesw")
        difficultyMenu=OptionMenu(self, difficultyVar,"Easy","Normal","Hard").grid(row=4,column=2,sticky="nesw")
        b1=Button(self,text="Done",command = self.exit).grid(row=5,column=2,sticky="nesw")
    
    
    def exit(self):
        config=open("Settings.txt","w")
            
        res=str(resolutionVar.get())
        dif=str(difficultyVar.get())
        full=str(fullScreen.get())
        #appear=str(showAgain.get())
        text=res+"z"+dif+"z"+full
        print(text)
        config.write(text)
        config.close()
    
        root.destroy()
        import MyGame
        #MyGame.main()
        

root=Tk()

fullScreen=IntVar()
#showAgain=IntVar()
resolutionVar=StringVar(root)
difficultyVar=StringVar(root)

#fail=True
if fail==False:
    resolutionVar.set(settings[0])
    difficultyVar.set(settings[1])
    fullScreen.set(settings[2])
elif fail==True:
    resolutionVar.set("1280x720")
    difficultyVar.set("Normal")
    fullScreen.set(0)

root.title("Game Launcher")
root.minsize(280, 180)
app=Application(root)

root.mainloop()
