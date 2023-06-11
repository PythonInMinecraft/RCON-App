"""The tk class"""

#Externals imports
try:
    from mcrcon import MCRcon
    from tkinter import *
except:
    print("Restart the app.")
    exit(-1)

class Interface(object):
    def __init__(self):
        self.wind = Tk()

        self.wind.title("RCON App")

        self.ask_state()

    def ask_state(self):
        """GUI when asking"""
        self.reset()
        self.l1 = Label(self.wind, text="Please enter the  server address")
        self.l1.pack()

        self.e1 = Entry(self.wind, width=30)
        self.e1.pack()

        self.l12 = Label(self.wind, text="Please enter the  rcon password")
        self.l12.pack()

        self.e2 = Entry(self.wind, width=30, show="*")
        self.e2.pack()

        self.ok = Button(self.wind, text="OK", command=self.ok_ask)
        self.ok.pack()

        mainloop()

    def reset(self):
        """Clear the GUI"""
        self.wind.destroy()
        self.wind = Tk()
        self.wind.title("RCON App")

    def ok_ask(self):
        """When the OK button is pressed"""
        self.ip = self.e1.get()
        self.password = self.e2.get()
        pass

        self.main()

    def main(self):
        """Main GUI"""
        self.reset()
        self.l1 = Label(self.wind, text="Command")
        self.l1.pack()

        self.e1 = Entry(self.wind, width="30")
        self.e1.pack()

        f = Frame(self.wind)
        f.pack()

        self.ok = Button(f, text="OK", command=self.ok_main)
        self.ok.pack()

        self.back = Button(f, text="BACK", command=self.ask_state)
        self.back.pack()

        mainloop()

    def ok_main(self):
        """When the OK main button is pressed"""
        with MCRcon(self.ip, self.password) as rcon:
            resp = rcon.command(self.e1.get())
            print(resp)
