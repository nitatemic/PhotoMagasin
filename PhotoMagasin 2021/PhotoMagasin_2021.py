from tkinter import *
from PIL import Image   # On importe la lib PIL

imgSource = Image.open(input())    # On ouvre l'image 
largeur,hauteur = imgSource.size 

Menu = Tk() # création de la fenêtre du menu 

TxtMenu = Label(Menu, text = 'Txt de bienvenue', fg = 'black')



def flou():
    imgFinalF = Image.new('RGB', (largeur,hauteur))
    
    for y in range(1, largeur - 1):
        for x in range(1, hauteur - 1):
            px = imgSource.getpixel((x,y))
            NewPxR = round((imgSource.getpixel((x - 1 ,y - 1))[0] + imgSource.getpixel((x , y - 1))[0] + imgSource.getpixel((x + 1 ,y - 1))[0] + imgSource.getpixel((x -1 , y))[0] + imgSource.getpixel((x + 1 ,y))[0] + imgSource.getpixel((x - 1 ,y + 1))[0] + imgSource.getpixel((x , y + 1))[0] + imgSource.getpixel((x + 1,y + 1))[0]) / 8)
            NewPxG = round((imgSource.getpixel((x - 1 ,y - 1))[1] + imgSource.getpixel((x , y - 1))[1] + imgSource.getpixel((x + 1 ,y - 1))[1] + imgSource.getpixel((x -1 , y))[1] + imgSource.getpixel((x + 1 ,y))[1] + imgSource.getpixel((x - 1 ,y + 1))[1] + imgSource.getpixel((x , y + 1))[1] + imgSource.getpixel((x + 1,y + 1))[1]) / 8)
            NewPxB = round((imgSource.getpixel((x - 1 ,y - 1))[2] + imgSource.getpixel((x , y - 1))[1] + imgSource.getpixel((x + 1 ,y - 1))[2] + imgSource.getpixel((x -1 , y))[2] + imgSource.getpixel((x + 1 ,y))[2] + imgSource.getpixel((x - 1 ,y + 1))[2] + imgSource.getpixel((x , y + 1))[2] + imgSource.getpixel((x + 1,y + 1))[2]) / 8)
            imgFinalF.putpixel((x , y), (NewPxR, NewPxG, NewPxB))

def contour():
   
    imgFinalC = Image.new('RGB', (largeur,hauteur))
    flou(imgSource)
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
