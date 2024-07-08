
# importing libraries
from tkinter import *
from tkinter import messagebox

# importing class functions
from classes.CreateMainWindow import CreateMainWindow
from functions.AddNewPokemon import addnewpokemon

if __name__ == '__main__':
    create_main_window = CreateMainWindow()

    create_main_window.mainloop()
