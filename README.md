# PhotoMagasin

## Introduction

PhotoMagasin est un project scolaire, il ne doit pas être utilisé quotidiennement sauf si vous adorer les icônes de chargement (Parce que le programme est long, très long...)

## Code Samples

```
def lien(): # Fonction pour changer la photo
    global largeur
    global hauteur
    global imgSource
    Lien = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Fichier PNG","*.png"),))
    imgSource = Image.open(Lien)    # On ouvre l'image 
    largeur, hauteur = imgSource.size
```
> The variables and comments are in French.
I may translate them into English if I find the time

## Installation

The program was made under Python 3.8, it works under Python 3.9.4

The program use :
> Tkinter

> PIL

If you ever run it under Python 2.7, tell me if it works 

Programme made by me and Matthieu Azzoun Minet