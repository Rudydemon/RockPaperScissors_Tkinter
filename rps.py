# Rock Paper Scissors
# Peri Smith - Python Project 1

import tkinter
import random

root = tkinter.Tk()
root.title("Rock Paper Scissors")

mainframe = tkinter.Frame(root)
mainframe.grid(column=2, row=3)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# row 1, column 1
l11 = tkinter.Label(root, text="Your Choice : ")
l11.grid(row=0, column=0, padx=2, pady=2)

# row 1, column 2
l12 = tkinter.Label(root, text="Computer Choice : ")
l12.grid(row=0, column=1, padx=2, pady=2)

# dropdown menu
tvar = tkinter.StringVar(root)
choices = [' Rock ', ' Paper ', 'Scissors']
tvar.set(' Rock ')  # default option
menu = tkinter.OptionMenu(root, tvar, *choices)
menu.grid(row=1, column=0, padx=2, pady=2)
var = tvar.get()


def callback():
    l22 = tkinter.Label(root, text="                 ")
    opp = random.choice(choices)
    l22 = tkinter.Label(root, text=opp)
    l22.grid(row=1, column=1, padx=2, pady=2)
    if var == opp:
        l31 = tkinter.Label(root, text=" TIE ")
        l31.grid(row=2, column=1, padx=2, pady=2)
    elif (var == ' Rock ' and opp == ' Paper ') or (var == ' Paper ' and opp == 'Scissors') or (var == 'Scissors' and opp == ' Rock '):
        l31 = tkinter.Label(root, text="LOSE")
        l31.grid(row=2, column=1, padx=2, pady=2)
    else:
        l31 = tkinter.Label(root, text="WIN")
        l31.grid(row=2, column=1, padx=2, pady=2)


# button
btn = tkinter.Button(text="GO!", command=callback)
btn.grid(row=2, column=2, padx=2, pady=2)

root.mainloop()
