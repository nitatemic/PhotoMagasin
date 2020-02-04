from tkinter import *
from tkinter import filedialog
from PIL import Image   # On importe la lib PIL


Menu = Tk() # création de la fenêtre du menu
Menu.geometry("900x100+400+400")
Menu.title('PhotoMagasin 2021')
Lien = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Fichier PNG","*.png"),))
TxtMenu = Label(Menu, text = "Bienvenue sur Photo Magasin 2021, vous pouvez désormais appliquer l'effet de votre choix sur votre photo.", fg = 'black')
TxtMenu.pack()
imgSource = Image.open(Lien)    # On ouvre l'image 
largeur, hauteur = imgSource.size 

def lien():
    Lien = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Fichier PNG","*.png"),))
    imgSource = Image.open(Lien)    # On ouvre l'image 
    largeur, hauteur = imgSource.size

   
def flou():     # Effet de flou
    imgFinalF = Image.new('RGB', (largeur, hauteur))   
    for x in range(1, largeur - 1):
        for y in range(1, hauteur - 1):
            px = imgSource.getpixel((x,y))
            NewPxRF = round((imgSource.getpixel((x - 1 ,y - 1))[0] + imgSource.getpixel((x , y - 1))[0] + imgSource.getpixel((x + 1 ,y - 1))[0] + imgSource.getpixel((x -1 , y))[0] + imgSource.getpixel((x + 1 ,y))[0] + imgSource.getpixel((x - 1 ,y + 1))[0] + imgSource.getpixel((x , y + 1))[0] + imgSource.getpixel((x + 1,y + 1))[0]) / 8)
            NewPxGF = round((imgSource.getpixel((x - 1 ,y - 1))[1] + imgSource.getpixel((x , y - 1))[1] + imgSource.getpixel((x + 1 ,y - 1))[1] + imgSource.getpixel((x -1 , y))[1] + imgSource.getpixel((x + 1 ,y))[1] + imgSource.getpixel((x - 1 ,y + 1))[1] + imgSource.getpixel((x , y + 1))[1] + imgSource.getpixel((x + 1,y + 1))[1]) / 8)
            NewPxBF = round((imgSource.getpixel((x - 1 ,y - 1))[2] + imgSource.getpixel((x , y - 1))[1] + imgSource.getpixel((x + 1 ,y - 1))[2] + imgSource.getpixel((x -1 , y))[2] + imgSource.getpixel((x + 1 ,y))[2] + imgSource.getpixel((x - 1 ,y + 1))[2] + imgSource.getpixel((x , y + 1))[2] + imgSource.getpixel((x + 1,y + 1))[2]) / 8)
            imgFinalF.putpixel((x , y), (NewPxRF, NewPxGF, NewPxBF))
    SaveLocaF = filedialog.asksaveasfilename(initialdir = "/",title = "Selectionner un emplacement de sauvegarde",filetypes = (("Fichier PNG","*.png"),), defaultextension='.png')
    imgFinalF.save(SaveLocaF)

def contour():  # Effet de detection des contour
    imgFinalC = Image.new('RGB', (largeur, hauteur))
    for x in range(1, largeur - 1):
        for y in range(1, hauteur - 1):
            px = imgSource.getpixel((x,y))
            NewPxRC = imgSource.getpixel((x, y + 1))[0] + imgSource.getpixel((x , y - 1))[0] + imgSource.getpixel((x - 1 , y))[0] + imgSource.getpixel((x + 1 ,y))[0] + imgSource.getpixel((x , y))[0] * (-4)
            NewPxGC = imgSource.getpixel((x, y + 1))[1] + imgSource.getpixel((x , y - 1))[1] + imgSource.getpixel((x - 1 , y))[1] + imgSource.getpixel((x + 1 ,y))[1] + imgSource.getpixel((x , y))[1] * (-4) 
            NewPxBC = imgSource.getpixel((x, y + 1))[2] + imgSource.getpixel((x , y - 1))[2] + imgSource.getpixel((x - 1 , y))[2] + imgSource.getpixel((x + 1 ,y))[2] + imgSource.getpixel((x , y))[2] * (-4) 
            imgFinalC.putpixel((x , y), (NewPxRC, NewPxGC, NewPxBC))
    SaveLocaC = filedialog.asksaveasfilename(initialdir = "/",title = "Selectionner un emplacement de sauvegarde",filetypes = (("Fichier PNG","*.png"),), defaultextension='.png')
    imgFinalC.save(SaveLocaC)


def relief():   # Effet de relief
    imgFinalR = Image.new('RGB', (largeur, hauteur))
    for x in range(1, largeur - 1):
        for y in range(1, hauteur - 1):
            px = imgSource.getpixel((x,y))
            NewPxRF = imgSource.getpixel((x , y - 1))[0] + imgSource.getpixel((x + 1 ,y - 1))[0] * (2) - imgSource.getpixel((x -1 , y))[0] + imgSource.getpixel((x + 1 ,y))[0] + imgSource.getpixel((x ,y))[0] + imgSource.getpixel((x - 1 ,y + 1))[0] *(-2) - imgSource.getpixel((x , y + 1))[0]
            NewPxGF = imgSource.getpixel((x , y - 1))[1] + imgSource.getpixel((x + 1 ,y - 1))[1] * (2) - imgSource.getpixel((x -1 , y))[1] + imgSource.getpixel((x + 1 ,y))[1] + imgSource.getpixel((x ,y))[1] + imgSource.getpixel((x - 1 ,y + 1))[1] *(-2) - imgSource.getpixel((x , y + 1))[1]
            NewPxBF = imgSource.getpixel((x , y - 1))[2] + imgSource.getpixel((x + 1 ,y - 1))[2] * (2) - imgSource.getpixel((x -1 , y))[2] + imgSource.getpixel((x + 1 ,y))[2] + imgSource.getpixel((x ,y))[2] + imgSource.getpixel((x - 1 ,y + 1))[2] *(-2) - imgSource.getpixel((x , y + 1))[2]
            imgFinalR.putpixel((x , y), (NewPxRF, NewPxGF, NewPxBF))
    SaveLocaR = filedialog.asksaveasfilename(initialdir = "/",title = "Selectionner un emplacement de sauvegarde",filetypes = (("Fichier PNG","*.png"),), defaultextension='.png')
    imgFinalR.save(SaveLocaR)

def contraste():   # Effet de contraste
    imgFinalCO = Image.new('RGB', (largeur, hauteur))
    for x in range(1, largeur - 1):
        for y in range(1, hauteur - 1):
            px = imgSource.getpixel((x,y))
            NewPxRCO = -imgSource.getpixel((x , y - 1))[0] - imgSource.getpixel((x - 1 , y))[0] - imgSource.getpixel((x + 1 ,y))[0] + imgSource.getpixel((x ,y))[0] * 5 - imgSource.getpixel((x , y + 1))[0]
            NewPxGCO = -imgSource.getpixel((x , y - 1))[1] - imgSource.getpixel((x - 1 , y))[1] - imgSource.getpixel((x + 1 ,y))[1] + imgSource.getpixel((x ,y))[1] * 5 - imgSource.getpixel((x , y + 1))[1]
            NewPxBCO = -imgSource.getpixel((x , y - 1))[2] - imgSource.getpixel((x - 1 , y))[2] - imgSource.getpixel((x + 1 ,y))[2] + imgSource.getpixel((x ,y))[2] * 5 - imgSource.getpixel((x , y + 1))[2]
            imgFinalCO.putpixel((x , y), (NewPxRCO, NewPxGCO, NewPxBCO))
    SaveLocaCO = filedialog.asksaveasfilename(initialdir = "/",title = "Selectionner un emplacement de sauvegarde",filetypes = (("Fichier PNG","*.png"),), defaultextension='.png')
    imgFinalCO.save(SaveLocaCO)

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