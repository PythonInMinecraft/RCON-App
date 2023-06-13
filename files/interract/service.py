"""The tk class"""

#Externals imports
try:
    from mcrcon import MCRcon, MCRconException
    from tkinter import *
    from tkinter import simpledialog as s
    from tkinter.scrolledtext import *
    from threading import Thread
    from time import *
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

        self.e2.bind("<Return>", self.ok_ask)

        self.ok = Button(self.wind, text="OK", command=self.ok_ask)
        self.ok.pack()

        self.wind.attributes("-topmost", True)

        mainloop()

    def reset(self):
        """Clear the GUI"""
        self.wind.destroy()
        self.wind = Tk()
        self.wind.title("RCON App")

    def ok_ask(self, e=None):
        """When the OK button is pressed"""
        self.ip = self.e1.get()
        self.password = self.e2.get()

        try:
            self.rcon = MCRcon(self.ip, self.password)
            self.rcon.connect()
            self.rcon.command("tag @a list")    #check the connection
            self.main()
            self.rcon.disconnect()
        except MCRconException:
            s.messagebox.showerror("Error", "Failed to login.")
            self.rcon.disconnect()
        except TimeoutError:
            s.messagebox.showerror("Error", "Server timed out.\nDid you enter the good ip ?")
        except OSError:
            s.messagebox.showerror("Error", "Invalid address.")


    def main(self):
        """Main GUI"""
        self.reset()
        self.l1 = Label(self.wind, text="Command")
        self.l1.pack()

        self.ef = Frame(self.wind)
        self.ef.pack()

        self.l = Label(self.ef, text="/")
        self.l.pack(side=LEFT)

        self.promptF = Frame(self.ef)
        self.promptF.pack()

        self.e1 = Entry(self.promptF, width="30")
        self.e1.pack(side=LEFT)

        self.e1.bind("<Return>", self.ok_main)

        self.scroll = ScrolledText(self.wind, width=50, height=30, state="disabled")
        self.scroll.pack()

        f = Frame(self.wind)
        f.pack()

        self.ok = Button(f, text="OK", command=self.ok_main)
        self.ok.pack(side=LEFT)

        self.back = Button(f, text="BACK", command=self.ask_state)
        self.back.pack(side=LEFT)

        self.wind.attributes("-topmost", True)

        mainloop()

    def ok_main(self, e=None):
        """When the OK main button is pressed"""
        resp = self.rcon.command(self.e1.get())
        t = self.e1.get() + "\n" + resp + "\n"
        self.print(resp)

        self.e1.destroy()

        self.e1 = Entry(self.promptF, width="30")
        self.e1.pack(side=LEFT)

        self.e1.bind("<Return>", self.ok_main)

    def print(self, text:str):
        """Print something in the scrolled text"""
        self.scroll.configure(state="normal")
        txt = self.e1.get() + " :\n" + text + "\n\n"
        self.scroll.insert(END, txt)
        self.scroll.configure(state="disabled")

import tkinter as tk

class Wait(tk.Tk):
    def __init__(self, rcon:MCRcon):
        super().__init__()
        self.title("Connecting")
        self.rcon = rcon

        self.show_please_wait_window()
        self.execute_background_process()

    def show_please_wait_window(self):
        self.please_wait_window = tk.Toplevel(self)
        label = tk.Label(self.please_wait_window, text="Connecting to server RCON...\nPlease wait.")
        label.pack()

    def update_ui(self):
        # Mettre à jour l'interface utilisateur en fonction de l'état du processus
        pass

    def execute_background_process(self):
        self.rcon.connect()
        self.please_wait_window.destroy()

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
