from tkinter import *
import customtkinter
from customtkinter import *

customtkinter.set_appearance_mode("dark")

main_window = CTk()

main_window.geometry("900x700")

button = CTkButton(master = main_window, text="Hello World")

button.place(relx=0.5, rely=0.5, anchor = CENTER)

main_window.mainloop()