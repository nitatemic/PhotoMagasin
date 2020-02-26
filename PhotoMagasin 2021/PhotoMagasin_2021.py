from tkinter import *
from tkinter import filedialog
from PIL import Image   # On importe la lib PIL

def lien(): # Fonction pour changer la photo
    global largeur
    global hauteur
    global imgSource
    Lien = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Fichier PNG","*.png"),))
    imgSource = Image.open(Lien)    # On ouvre l'image 
    largeur, hauteur = imgSource.size
    
Menu = Tk() # Création de la fenêtre du menu
Menu.geometry("900x100+400+400")
Menu.title('PhotoMagasin 2021')
TxtMenu = Label(Menu, text = "Bienvenue sur PhotoMagasin 2021, vous pouvez désormais appliquer l'effet de votre choix sur votre photo.", fg = 'black')
TxtMenu.pack()
lien()



   
def flou():     # Effet de flou
    imgFinalF = Image.new('RGB', (largeur, hauteur))   
    for x in range(1, largeur - 1): # On crée une boucle qui prend en charge le nombre de pixel horizontaux
        for y in range(1, hauteur - 1): # idem mais pour le nbr de pixels verticaux
            px = imgSource.getpixel((x,y))
            # Matrice convolution de pixel en 3*3
            NewPxRF = round((imgSource.getpixel((x - 1 ,y - 1))[0] + imgSource.getpixel((x , y - 1))[0] + imgSource.getpixel((x + 1 ,y - 1))[0] + imgSource.getpixel((x -1 , y))[0] + imgSource.getpixel((x + 1 ,y))[0] + imgSource.getpixel((x - 1 ,y + 1))[0] + imgSource.getpixel((x , y + 1))[0] + imgSource.getpixel((x + 1,y + 1))[0]) / 8)
            NewPxGF = round((imgSource.getpixel((x - 1 ,y - 1))[1] + imgSource.getpixel((x , y - 1))[1] + imgSource.getpixel((x + 1 ,y - 1))[1] + imgSource.getpixel((x -1 , y))[1] + imgSource.getpixel((x + 1 ,y))[1] + imgSource.getpixel((x - 1 ,y + 1))[1] + imgSource.getpixel((x , y + 1))[1] + imgSource.getpixel((x + 1,y + 1))[1]) / 8)
            NewPxBF = round((imgSource.getpixel((x - 1 ,y - 1))[2] + imgSource.getpixel((x , y - 1))[1] + imgSource.getpixel((x + 1 ,y - 1))[2] + imgSource.getpixel((x -1 , y))[2] + imgSource.getpixel((x + 1 ,y))[2] + imgSource.getpixel((x - 1 ,y + 1))[2] + imgSource.getpixel((x , y + 1))[2] + imgSource.getpixel((x + 1,y + 1))[2]) / 8)
            imgFinalF.putpixel((x , y), (NewPxRF, NewPxGF, NewPxBF)) # Création de la nouvelle image
    SaveLocaF = filedialog.asksaveasfilename(initialdir = "/",title = "Selectionner un emplacement de sauvegarde",filetypes = (("Fichier PNG","*.png"),), defaultextension='.png') # Explorateur pour choisir ou sauvegarder la photo
    imgFinalF.save(SaveLocaF)
    imgFinalF.show() # On montre l'image modifiée
    

def contour():  # Effet de detection des contour
    imgFinalC = Image.new('RGB', (largeur, hauteur))
    for x in range(1, largeur - 1): # On crée une boucle qui prend en charge le nombre de pixel horizontaux
        for y in range(1, hauteur - 1): # idem mais pour le nbr de pixels verticaux
            px = imgSource.getpixel((x,y))
            # Matrice convolution de pixel en 3*3
            NewPxRC = imgSource.getpixel((x, y + 1))[0] + imgSource.getpixel((x , y - 1))[0] + imgSource.getpixel((x - 1 , y))[0] + imgSource.getpixel((x + 1 ,y))[0] + imgSource.getpixel((x , y))[0] * (-4)
            NewPxGC = imgSource.getpixel((x, y + 1))[1] + imgSource.getpixel((x , y - 1))[1] + imgSource.getpixel((x - 1 , y))[1] + imgSource.getpixel((x + 1 ,y))[1] + imgSource.getpixel((x , y))[1] * (-4) 
            NewPxBC = imgSource.getpixel((x, y + 1))[2] + imgSource.getpixel((x , y - 1))[2] + imgSource.getpixel((x - 1 , y))[2] + imgSource.getpixel((x + 1 ,y))[2] + imgSource.getpixel((x , y))[2] * (-4) 
            imgFinalC.putpixel((x , y), (NewPxRC, NewPxGC, NewPxBC)) # Création de la nouvelle image
    SaveLocaC = filedialog.asksaveasfilename(initialdir = "/",title = "Selectionner un emplacement de sauvegarde",filetypes = (("Fichier PNG","*.png"),), defaultextension='.png') # Explorateur pour choisir ou sauvegarder la photo
    imgFinalC.save(SaveLocaC)
    imgFinalC.show() # On montre l'image modifiée


def relief():   # Effet de relief
    imgFinalR = Image.new('RGB', (largeur, hauteur))
    for x in range(1, largeur - 1): # On crée une boucle qui prend en charge le nombre de pixel horizontaux
        for y in range(1, hauteur - 1): # idem mais pour le nbr de pixels verticaux
            px = imgSource.getpixel((x,y))
            # Matrice convolution de pixel en 3*3
            NewPxRF = imgSource.getpixel((x , y - 1))[0] + imgSource.getpixel((x + 1 ,y - 1))[0] * (2) - imgSource.getpixel((x -1 , y))[0] + imgSource.getpixel((x + 1 ,y))[0] + imgSource.getpixel((x ,y))[0] + imgSource.getpixel((x - 1 ,y + 1))[0] *(-2) - imgSource.getpixel((x , y + 1))[0]
            NewPxGF = imgSource.getpixel((x , y - 1))[1] + imgSource.getpixel((x + 1 ,y - 1))[1] * (2) - imgSource.getpixel((x -1 , y))[1] + imgSource.getpixel((x + 1 ,y))[1] + imgSource.getpixel((x ,y))[1] + imgSource.getpixel((x - 1 ,y + 1))[1] *(-2) - imgSource.getpixel((x , y + 1))[1]
            NewPxBF = imgSource.getpixel((x , y - 1))[2] + imgSource.getpixel((x + 1 ,y - 1))[2] * (2) - imgSource.getpixel((x -1 , y))[2] + imgSource.getpixel((x + 1 ,y))[2] + imgSource.getpixel((x ,y))[2] + imgSource.getpixel((x - 1 ,y + 1))[2] *(-2) - imgSource.getpixel((x , y + 1))[2]
            imgFinalR.putpixel((x , y), (NewPxRF, NewPxGF, NewPxBF)) # Création de la nouvelle image
    SaveLocaR = filedialog.asksaveasfilename(initialdir = "/",title = "Selectionner un emplacement de sauvegarde",filetypes = (("Fichier PNG","*.png"),), defaultextension='.png') # Explorateur pour choisir ou sauvegarder la photo
    imgFinalR.save(SaveLocaR)
    imgFinalR.show() # On montre l'image modifiée

def contraste():   # Effet de contraste
    imgFinalCO = Image.new('RGB', (largeur, hauteur))
    for x in range(1, largeur - 1): # On crée une boucle qui prend en charge le nombre de pixel horizontaux
        for y in range(1, hauteur - 1): # idem mais pour le nbr de pixels verticaux
            px = imgSource.getpixel((x,y))
            # Matrice convolution de pixel en 3*3
            NewPxRCO = -imgSource.getpixel((x , y - 1))[0] - imgSource.getpixel((x - 1 , y))[0] - imgSource.getpixel((x + 1 ,y))[0] + imgSource.getpixel((x ,y))[0] * 5 - imgSource.getpixel((x , y + 1))[0]
            NewPxGCO = -imgSource.getpixel((x , y - 1))[1] - imgSource.getpixel((x - 1 , y))[1] - imgSource.getpixel((x + 1 ,y))[1] + imgSource.getpixel((x ,y))[1] * 5 - imgSource.getpixel((x , y + 1))[1]
            NewPxBCO = -imgSource.getpixel((x , y - 1))[2] - imgSource.getpixel((x - 1 , y))[2] - imgSource.getpixel((x + 1 ,y))[2] + imgSource.getpixel((x ,y))[2] * 5 - imgSource.getpixel((x , y + 1))[2]
            imgFinalCO.putpixel((x , y), (NewPxRCO, NewPxGCO, NewPxBCO)) # Création de la nouvelle image
    SaveLocaCO = filedialog.asksaveasfilename(initialdir = "/",title = "Selectionner un emplacement de sauvegarde",filetypes = (("Fichier PNG","*.png"),), defaultextension='.png') # Explorateur pour choisir ou sauvegarder la photo
    imgFinalCO.save(SaveLocaCO)
    imgFinalCO.show() # On montre l'image modifiée

BtnFl = Button(Menu, text = 'Flouter la photo', command = flou)
BtnFl.pack(side = LEFT, padx = 20, pady = 5)
BtnCtr = Button(Menu, text = 'Mettre en avant les contours de la photo', command = contour)
BtnCtr.pack(side = LEFT, padx = 10,pady = 5)
BtnSp = Button(Menu, text = 'Choisir une photo', command = lien)
BtnSp.pack(side = LEFT, padx = 10,pady = 5)
BtnRlf = Button(Menu, text = 'Ajouter des reliefs à la photo', command = relief)
BtnRlf.pack(side = LEFT, padx = 10,pady = 5)
BtnCtrst = Button(Menu, text = 'Changer le contraste de la photo', command = contraste)
BtnCtrst.pack(side = LEFT, padx = 10,pady = 5)
Menu.resizable(width=False, height=False)
Menu.mainloop()

#  Progrmamme terminée le 06/02/2020 à 11:16
# © Lemenyalex et Matthieu Azzoun Minet 