from PIL import Image   # On importe la lib PIL


imgSource = Image.open("chien.png")    # On ouvre l'image fruits.png
largeur,hauteur = imgSource.size        # On recupere la taille de l'image (En pixel)
imgFinal = Image.new('RGB', (largeur,hauteur))
