from tkinter import *
from PIL import Image   # On importe la lib PIL

ImgVanilla = input()# Lien de la photo d'origine

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

def flou():
    imgSource = Image.open(ImgVanilla)    # On ouvre l'image fruits.png
    largeur,hauteur = imgSource.size        # On recupere la taille de l'image (En pixel)
    imgFinal = Image.new('RGB', (largeur,hauteur))

    for y in range(1, largeur - 1):
        for x in range(1, hauteur - 1):
            px = imgSource.getpixel((x,y))
            NewPxR = round((imgSource.getpixel((x - 1 ,y - 1))[0] + imgSource.getpixel((x , y - 1))[0] + imgSource.getpixel((x + 1 ,y - 1))[0] + imgSource.getpixel((x -1 , y))[0] + imgSource.getpixel((x + 1 ,y))[0] + imgSource.getpixel((x - 1 ,y + 1))[0] + imgSource.getpixel((x , y + 1))[0] + imgSource.getpixel((x + 1,y + 1))[0]) / 8)
            NewPxG = round((imgSource.getpixel((x - 1 ,y - 1))[1] + imgSource.getpixel((x , y - 1))[1] + imgSource.getpixel((x + 1 ,y - 1))[1] + imgSource.getpixel((x -1 , y))[1] + imgSource.getpixel((x + 1 ,y))[1] + imgSource.getpixel((x - 1 ,y + 1))[1] + imgSource.getpixel((x , y + 1))[1] + imgSource.getpixel((x + 1,y + 1))[1]) / 8)
            NewPxB = round((imgSource.getpixel((x - 1 ,y - 1))[2] + imgSource.getpixel((x , y - 1))[1] + imgSource.getpixel((x + 1 ,y - 1))[2] + imgSource.getpixel((x -1 , y))[2] + imgSource.getpixel((x + 1 ,y))[2] + imgSource.getpixel((x - 1 ,y + 1))[2] + imgSource.getpixel((x , y + 1))[2] + imgSource.getpixel((x + 1,y + 1))[2]) / 8)
            imgFinal.putpixel((x , y), (NewPxR, NewPxG, NewPxB))
    imgFinal.save(ImgNew)
    imgFinal.show()
