from PIL import *   # On importe la lib PIL


imgSource = Image.open("chien.png")    # On ouvre l'image fruits.png
largeur,hauteur = imgSource.size        # On recupere la taille de l'image (En pixel)
imgFinal = Image.new('RGB', (largeur,hauteur))

for x in range(1, largeur - 1):
    for y in range(1, hauteur - 1):
        px = imgSource.getpixel((y,x))
