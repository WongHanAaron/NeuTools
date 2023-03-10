from tkinter import *
import customtkinter
from customtkinter import *

class MainApplication(CTkFrame):
    def __init__(self, parent, *args, **kwargs):
        CTkFrame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        customtkinter.set_appearance_mode("dark")
        
        self.parent.geometry("900x700")

        button = CTkButton(master = self, text="Hello World")

        button.place(relx=0.5, rely=0.5, anchor = CENTER)

if __name__ == "__main__":
    root = CTk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
