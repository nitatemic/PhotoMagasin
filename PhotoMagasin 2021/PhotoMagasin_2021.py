from tkinter import *

# Main window
Main = Tk()

#Presentation
MainLabel = Label(Main, text = 'Bienvenue dans PhotoMagasin 2021')
MainLabel.pack()
#Bouton Exit
ExitButton = Button(Main, text = 'Quitter', command = Main.destroy)
ExitButton.pack()

# Gestionnaire d'évenement
Main.mainloop()