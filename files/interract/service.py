"""The tk class"""

#Externals imports
try:
    from mcrcon import MCRcon, MCRconException
    from tkinter import *
    from tkinter import simpledialog as s
    from tkinter.scrolledtext import *
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

        self.e2 = Entry(self.wind, width=30, show="•")
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

        try:
            self.rcon = MCRcon(self.ip, self.password)
            self.rcon.connect()
            self.rcon.command("tag @a list")    #check the connection
            self.main()
        except MCRconException:
            s.messagebox.showerror("Error", "Failed to login")
        self.rcon.disconnect()


    def main(self):
        """Main GUI"""
        self.reset()
        self.l1 = Label(self.wind, text="Command")
        self.l1.pack()

        self.ef = Frame(self.wind)
        self.ef.pack()

        self.l = Label(self.ef, text="/")
        self.l.pack(side=LEFT)

        self.e1 = Entry(self.ef, width="30")
        self.e1.pack(side=LEFT)

        self.scroll = ScrolledText(self.wind, width=50, height=30, state="disabled")
        self.scroll.pack()

        f = Frame(self.wind)
        f.pack()

        self.ok = Button(f, text="OK", command=self.ok_main)
        self.ok.pack(side=LEFT)

        self.back = Button(f, text="BACK", command=self.ask_state)
        self.back.pack(side=LEFT)

        mainloop()

    def ok_main(self):
        """When the OK main button is pressed"""
        resp = self.rcon.command(self.e1.get())
        t = self.e1.get() + "\n" + resp + "\n"
        self.print(resp)

    def print(self, text:str):
        """Print something in the scrolled text"""
        self.scroll.configure(state="normal")
        self.scroll.insert(END, text + "\n")
        self.scroll.configure(state="disabled")