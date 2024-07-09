# importing libraries
from tkinter import *
from tkinter import messagebox

# importing class functions
from classes.CreateMainWindow import CreateMainWindow
from functions.AddNewPokemon import addnewpokemon
from functions.CheckInput import checkinput


def preppokemon(pokemon_types):
    types = pokemon_types

    type1 = format(pokemon1_type1.get())
    type2 = format(pokemon1_type2.get())

    valid = checkinput(type1, type2)

    if valid == "quit":
        create_main_window.quit()

    if valid:
        addnewpokemon(type1, type2)
    else:
        messagebox.showinfo("WARNING", "something wrong with one of the selected types")


if __name__ == '__main__':
    # create the main window, nothing should be above this line except the if statement
    create_main_window = CreateMainWindow()

    # defining the grid
    create_main_window.columnconfigure((0, 1, 2, 3, 4), weight=1)
    create_main_window.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8), weight=1)

    # title text
    label_var = StringVar()
    add_types_label = Label(create_main_window, textvariable=label_var, font="bold")
    label_var.set("select the pokemon types below:")

    # input fields (for up to 6 Pokémon, copy past the code below to add more fields)

    # input fields | labels (names)
    label_var = StringVar()
    pokemon1_type1_label = Label(create_main_window, textvariable=label_var, font="bold")
    label_var.set("type 1:")

    label_var = StringVar()
    pokemon1_type2_label = Label(create_main_window, textvariable=label_var, font="bold")
    label_var.set("type 2:")

    # input fields | logic (functionality)
    pokemon_types = ["normal", "fire", "water", "grass", "electric", "ice", "fighting", "poison", "ground", "flying",
                     "psychic", "bug", "rock", "ghost", "dragon", "dark", "steel", "fairy"]

    pokemon1_type1 = StringVar()
    pokemon1_type1.set("none")
    pokemon1_type1_field = OptionMenu(create_main_window, pokemon1_type1, *pokemon_types)

    pokemon1_type2 = StringVar()
    pokemon1_type2.set("none")
    pokemon1_type2_field = OptionMenu(create_main_window, pokemon1_type2, *pokemon_types)

    button_text = StringVar()
    button_text.set("submit types")

    # submit button
    submit_button = Button(create_main_window, textvariable=button_text, command=lambda: preppokemon(pokemon_types))

    # placing everything on the grid

    pokemon1_type1_label.grid(row=1, column=1, sticky="snew")
    pokemon1_type1_field.grid(row=1, column=2, sticky="snew")
    pokemon1_type2_label.grid(row=1, column=3, sticky="snew")
    pokemon1_type2_field.grid(row=1, column=4, sticky="snew")

    submit_button.grid(row=3, column=1, sticky="snew")

    # running the main loop, nothing should be below this line except the mainloop execute
    create_main_window.mainloop()
