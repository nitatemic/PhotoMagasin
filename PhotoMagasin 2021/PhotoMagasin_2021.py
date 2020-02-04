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
largeur,hauteur = imgSource.size 



def flou():     # Effet de flou
    imgFinalF = Image.new('RGB', (largeur,hauteur))   
    for x in range(1, largeur - 1):
        for y in range(1, hauteur - 1):
            px = imgSource.getpixel((x,y))
            NewPxR = round((imgSource.getpixel((x - 1 ,y - 1))[0] + imgSource.getpixel((x , y - 1))[0] + imgSource.getpixel((x + 1 ,y - 1))[0] + imgSource.getpixel((x -1 , y))[0] + imgSource.getpixel((x + 1 ,y))[0] + imgSource.getpixel((x - 1 ,y + 1))[0] + imgSource.getpixel((x , y + 1))[0] + imgSource.getpixel((x + 1,y + 1))[0]) / 8)
            NewPxG = round((imgSource.getpixel((x - 1 ,y - 1))[1] + imgSource.getpixel((x , y - 1))[1] + imgSource.getpixel((x + 1 ,y - 1))[1] + imgSource.getpixel((x -1 , y))[1] + imgSource.getpixel((x + 1 ,y))[1] + imgSource.getpixel((x - 1 ,y + 1))[1] + imgSource.getpixel((x , y + 1))[1] + imgSource.getpixel((x + 1,y + 1))[1]) / 8)
            NewPxB = round((imgSource.getpixel((x - 1 ,y - 1))[2] + imgSource.getpixel((x , y - 1))[1] + imgSource.getpixel((x + 1 ,y - 1))[2] + imgSource.getpixel((x -1 , y))[2] + imgSource.getpixel((x + 1 ,y))[2] + imgSource.getpixel((x - 1 ,y + 1))[2] + imgSource.getpixel((x , y + 1))[2] + imgSource.getpixel((x + 1,y + 1))[2]) / 8)
            imgFinalF.putpixel((x , y), (NewPxR, NewPxG, NewPxB))
    SaveLocaF = filedialog.asksaveasfilename(initialdir = "/",title = "Selectionner un emplacement de sauvegarde",filetypes = (("Fichier PNG","*.png"),), defaultextension='.png')
    imgFinalF.save(SaveLocaF)

def contour():  # Effet de detection des contour
   
    imgFinalC = Image.new('RGB', (largeur,hauteur))
    flou()
    imgFinalF = Image.open("imgFlou.png")
    for l in range(1, largeur - 1):
        for h in range(1, hauteur - 1):
            PxFR = imgFinalF((l, h))[0]
            PxR = imgSource((l, h))[0]
            PxFG = imgFinalF((l, h))[1]
            PxG = imgSource((l, h))[1]
            PxFB = imgFinalF((l, h))[2]
            PxB = imgSource((l, h))[2]
            NewPxR = abs(PxR - PxFR)
            NewPxG = abs(PxG - PxFG)
            NewPxB = abs(PxB - PxFB)
            imgFinalC.putpixel((h , l),(NewPxR, NewPxG, NewPxB))

#def relief():   # Effet de relief
#    imgFinalR = Image.new('RGB', (largeur, hauteur))

#    for l in range(1, largeur - 1):
#        for h in range(1, hauteur - 1):
#            px = imgSource.getpixel((x,y))




BtnFl = Button(Menu, text = 'Flouter la photo', command = flou)
BtnFl.pack(side = LEFT, padx = 10, pady = 5)
BtnCtr = Button(Menu, text = 'Mettre en avant les contours de la photo', command = contour)
BtnCtr.pack()
# BtnRlf = Button(Menu, text = 'Ajouter des reliefs à la photo', command = relief)
# BtnRlf.pack()

Menu.mainloop()