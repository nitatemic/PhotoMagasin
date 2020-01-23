from tkinter import *
from PIL import Image   # On importe la lib PIL

ImgVanilla = Image.open(input())    # On ouvre l'image vanilla
largeur,hauteur = imgSource.size 

def flou():
    imgFinalF = Image.new('RGB', (largeur,hauteur))


    for y in range(1, largeur - 1):
        for x in range(1, hauteur - 1):
            px = imgSource.getpixel((x,y))
            NewPxR = round((imgSource.getpixel((x - 1 ,y - 1))[0] + imgSource.getpixel((x , y - 1))[0] + imgSource.getpixel((x + 1 ,y - 1))[0] + imgSource.getpixel((x -1 , y))[0] + imgSource.getpixel((x + 1 ,y))[0] + imgSource.getpixel((x - 1 ,y + 1))[0] + imgSource.getpixel((x , y + 1))[0] + imgSource.getpixel((x + 1,y + 1))[0]) / 8)
            NewPxG = round((imgSource.getpixel((x - 1 ,y - 1))[1] + imgSource.getpixel((x , y - 1))[1] + imgSource.getpixel((x + 1 ,y - 1))[1] + imgSource.getpixel((x -1 , y))[1] + imgSource.getpixel((x + 1 ,y))[1] + imgSource.getpixel((x - 1 ,y + 1))[1] + imgSource.getpixel((x , y + 1))[1] + imgSource.getpixel((x + 1,y + 1))[1]) / 8)
            NewPxB = round((imgSource.getpixel((x - 1 ,y - 1))[2] + imgSource.getpixel((x , y - 1))[1] + imgSource.getpixel((x + 1 ,y - 1))[2] + imgSource.getpixel((x -1 , y))[2] + imgSource.getpixel((x + 1 ,y))[2] + imgSource.getpixel((x - 1 ,y + 1))[2] + imgSource.getpixel((x , y + 1))[2] + imgSource.getpixel((x + 1,y + 1))[2]) / 8)
            imgFinal.putpixel((x , y), (NewPxR, NewPxG, NewPxB))
    imgFinal.save(ImgNew)
    imgFinal.show()

def contour():
   
    imgFinalC = Image.new('RGB', (largeur,hauteur))
    flou(imgVanilla)
    for l in range(1, largeur - 1):
        for h in range(1, hauteur - 1):
            pf = imgFinalF((l, h))
            p = imgVanilla((l, h))
            