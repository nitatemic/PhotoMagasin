from tkinter import *
from tkinter import filedialog


from PIL import Image   # On importe la lib PIL

Menu = Tk() # création de la fenêtre du menu
Menu.geometry("800x100+400+400")
Menu.title('Bienvenue sur PhotoMagasin 2021 !')
Lien = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Fichier PNG","*.png"),))
TxtMenu = Label(Menu, text = "Bienvenue sur Photo Magasin 2021, vous pouvez désormais appliquer l'effet de votre choix sur votre photo.", fg = 'black')
TxtMenu.pack()
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
    imgNB = Image.new('RGB', (largeur, hauteur)) 
    
    for i in range (hauteur):   # On creer une boucle du nombre de pixel de la hauteur 
        for j in range(largeur):    # On creer une boucle du nombre de pixel de la largeur
            px = imgSource.getpixel((j,i))  # On prendre un pixel de coordonnées (j,i)
            R = round((px[0] + px[1] + px[2]) / 3)  # On fait la moyenne des valeurs des couleurs et on l'applique à chaque couleur du nouvau pixel
            pxGris = (R,R,R)    # On attribut les nouvelles naleurs dans le pixel de la nouvelle image
            imgNB.putpixel((j,i), (pxGris, pxGris, pxGris))  # On met le pixel dans la nouvelle image

    for x in range(1, largeur - 1):
        for y in range(1, hauteur - 1):
           NewPxC = round(imgNB.getpixel((x , y - 1))[0]  + imgNB.getpixel((x -1 , y))[0] + imgNB.getpixel((x + 1 ,y))[0] + imgNB.getpixel((x , y + 1))[0] + (imgNB.getpixel((x , y))[0] * (-4)))
           if NewPxC < 0:
               NewPxC = 0
           elif NewPxC > 255:
                NexPxC = 255
           # NewPxGC = round(imgSource.getpixel((x , y - 1))[1]  + imgSource.getpixel((x -1 , y))[1] + imgSource.getpixel((x + 1 ,y))[1] + imgSource.getpixel((x , y + 1))[1] + (imgSource.getpixel((x , y))[0] * (-4)))
           # NewPxBC = round(imgSource.getpixel((x , y - 1))[1]  + imgSource.getpixel((x -1 , y))[2] + imgSource.getpixel((x + 1 ,y))[2] + imgSource.getpixel((x , y + 1))[2] + (imgSource.getpixel((x , y))[0] * (-4)))
           imgFinalC.putpixel((x , y), (NewPxC, NewPxC, NewPxC))
    SaveLocaC = filedialog.asksaveasfilename(initialdir = "/",title = "Selectionner un emplacement de sauvegarde",filetypes = (("Fichier PNG","*.png"),), defaultextension='.png')
    imgFinalC.save(SaveLocaC)

def relief():   # Effet de relief
    imgFinalR = Image.new('RGB', (largeur, hauteur))
    for x in range(1, largeur - 1):
        for y in range(1, hauteur - 1):
            px = imgSource.getpixel((x,y))
            NewPxRF = (imgSource.getpixel((x - 1 ,y - 1))[0] * (0) + imgSource.getpixel((x , y - 1))[0] + imgSource.getpixel((x + 1 ,y - 1))[0] * (2) + imgSource.getpixel((x -1 , y))[0] * (-1) + imgSource.getpixel((x + 1 ,y))[0] + imgSource.getpixel((x ,y))[0] * (0) + imgSource.getpixel((x - 1 ,y + 1))[0] *(-2) + imgSource.getpixel((x , y + 1))[0] * (-1) + imgSource.getpixel((x + 1,y + 1))[0] * (0) )
            NewPxGF = (imgSource.getpixel((x - 1 ,y - 1))[1] * (0) + imgSource.getpixel((x , y - 1))[1] + imgSource.getpixel((x + 1 ,y - 1))[1] * (2) + imgSource.getpixel((x -1 , y))[1] * (-1) + imgSource.getpixel((x + 1 ,y))[1] + imgSource.getpixel((x ,y))[1] * (0) + imgSource.getpixel((x - 1 ,y + 1))[1] *(-2) + imgSource.getpixel((x , y + 1))[1] * (-1) + imgSource.getpixel((x + 1,y + 1))[1] * (0) )
            NewPxBF = (imgSource.getpixel((x - 1 ,y - 1))[2] * (0) + imgSource.getpixel((x , y - 1))[2] + imgSource.getpixel((x + 1 ,y - 1))[2] * (2) + imgSource.getpixel((x -1 , y))[2] * (-1) + imgSource.getpixel((x + 1 ,y))[2] + imgSource.getpixel((x ,y))[2] * (0) + imgSource.getpixel((x - 1 ,y + 1))[2] *(-2) + imgSource.getpixel((x , y + 1))[2] * (-1) + imgSource.getpixel((x + 1,y + 1))[2] * (0) )
            imgFinalR.putpixel((x , y), (NewPxRF, NewPxGF, NewPxBF))
    SaveLocaR = filedialog.asksaveasfilename(initialdir = "/",title = "Selectionner un emplacement de sauvegarde",filetypes = (("Fichier PNG","*.png"),), defaultextension='.png')
    imgFinalR.save(SaveLocaR)


def lien():
    Lien = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Fichier PNG","*.png"),))

BtnFl = Button(Menu, text = 'Flouter la photo', command = flou)
BtnFl.pack(side = LEFT, padx = 10, pady = 5)
BtnCtr = Button(Menu, text = 'Mettre en avant les contours de la photo', command = contour)
BtnCtr.pack(side = LEFT, padx = 10,pady = 5)
BtnSp = Button(Menu, text = 'Choisir une photo', command = lien)
BtnSp.pack(side = LEFT, padx = 10,pady = 5)
BtnRlf = Button(Menu, text = 'Ajouter des reliefs à la photo', command = relief)
BtnRlf.pack(side = LEFT, padx = 10,pady = 5)



Menu.mainloop()