from tkinter import *
from tkinter import filedialog
from PIL import Image  # On importe la lib PIL (Depuis pillow)


def lien():  # Fonction pour changer la photo
    global largeur
    global hauteur
    global img_source
    lien = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("Fichier PNG", "*.png"),))
    img_source = Image.open(lien)  # On ouvre l'image
    largeur, hauteur = img_source.size


Menu = Tk()  # Création de la fenêtre du menu
Menu.geometry("900x100+400+400")
Menu.title('PhotoMagasin 2021')
TxtMenu = Label(Menu,
                text="Bienvenue sur PhotoMagasin 2021, vous pouvez désormais appliquer l'effet de votre choix sur "
                     "votre photo.",
                fg='black')
TxtMenu.pack()
lien()


def flou():  # Effet de flou
    img_final_f = Image.new('RGB', (largeur, hauteur))
    for x in range(1, largeur - 1):  # On crée une boucle qui prend en charge le nombre de pixel horizontaux
        for y in range(1, hauteur - 1):  # idem mais pour le nbr de pixels verticaux
            px = img_source.getpixel((x, y))
            # Matrice convolution de pixel en 3*3
            new_px_rf = round((img_source.getpixel((x - 1, y - 1))[0] + img_source.getpixel((x, y - 1))[0] +
                               img_source.getpixel((x + 1, y - 1))[0] + img_source.getpixel((x - 1, y))[0] +
                               img_source.getpixel((x + 1, y))[0] + img_source.getpixel((x - 1, y + 1))[0] +
                               img_source.getpixel((x, y + 1))[0] + img_source.getpixel((x + 1, y + 1))[0]) / 9)
            new_px_gf = round((img_source.getpixel((x - 1, y - 1))[1] + img_source.getpixel((x, y - 1))[1] +
                               img_source.getpixel((x + 1, y - 1))[1] + img_source.getpixel((x - 1, y))[1] +
                               img_source.getpixel((x + 1, y))[1] + img_source.getpixel((x - 1, y + 1))[1] +
                               img_source.getpixel((x, y + 1))[1] + img_source.getpixel((x + 1, y + 1))[1]) / 9)
            new_px_bf = round((img_source.getpixel((x - 1, y - 1))[2] + img_source.getpixel((x, y - 1))[2] +
                               img_source.getpixel((x + 1, y - 1))[2] + img_source.getpixel((x - 1, y))[2] +
                               img_source.getpixel((x + 1, y))[2] + img_source.getpixel((x - 1, y + 1))[2] +
                               img_source.getpixel((x, y + 1))[2] + img_source.getpixel((x + 1, y + 1))[2]) / 9)
            img_final_f.putpixel((x, y), (new_px_rf, new_px_gf, new_px_bf))  # Création de la nouvelle image
    save_loca_f = filedialog.asksaveasfilename(initialdir="/", title="Sélectionner un emplacement de sauvegarde",
                                               filetypes=(("Fichier PNG", "*.png"),),
                                               defaultextension='.png')  # Explorateur pour choisir ou sauvegarder la photo
    img_final_f.save(save_loca_f)
    img_final_f.show()  # On montre l'image modifiée


def contour():  # Effet de detection des contour
    img_final_c = Image.new('RGB', (largeur, hauteur))
    for x in range(1, largeur - 1):  # On crée une boucle qui prend en charge le nombre de pixel horizontaux
        for y in range(1, hauteur - 1):  # idem mais pour le nbr de pixels verticaux
            px = img_source.getpixel((x, y))
            # Matrice convolution de pixel en 3*3
            new_px_rc = img_source.getpixel((x, y + 1))[0] + img_source.getpixel((x, y - 1))[0] + \
                        img_source.getpixel((x - 1, y))[0] + img_source.getpixel((x + 1, y))[0] + \
                        img_source.getpixel((x, y))[0] * (-4)
            new_px_gc = img_source.getpixel((x, y + 1))[1] + img_source.getpixel((x, y - 1))[1] + \
                        img_source.getpixel((x - 1, y))[1] + img_source.getpixel((x + 1, y))[1] + \
                        img_source.getpixel((x, y))[1] * (-4)
            new_px_bc = img_source.getpixel((x, y + 1))[2] + img_source.getpixel((x, y - 1))[2] + \
                        img_source.getpixel((x - 1, y))[2] + img_source.getpixel((x + 1, y))[2] + \
                        img_source.getpixel((x, y))[2] * (-4)
            img_final_c.putpixel((x, y), (new_px_rc, new_px_gc, new_px_bc))  # Création de la nouvelle image
    save_loca_c = filedialog.asksaveasfilename(initialdir="/", title="Sélectionner un emplacement de sauvegarde",
                                               filetypes=(("Fichier PNG", "*.png"),),
                                               defaultextension='.png')  # Explorateur pour choisir ou sauvegarder la photo
    img_final_c.save(save_loca_c)
    img_final_c.show()  # On montre l'image modifiée


def relief():  # Effet de relief
    img_final_r = Image.new('RGB', (largeur, hauteur))
    for x in range(1, largeur - 1):  # On crée une boucle qui prend en charge le nombre de pixel horizontaux
        for y in range(1, hauteur - 1):  # idem mais pour le nbr de pixels verticaux
            px = img_source.getpixel((x, y))
            # Matrice convolution de pixel en 3*3
            new_px_rf = img_source.getpixel((x, y - 1))[0] + img_source.getpixel((x + 1, y - 1))[0] * (2) - \
                      img_source.getpixel((x - 1, y))[0] + img_source.getpixel((x + 1, y))[0] + \
                      img_source.getpixel((x, y))[0] + img_source.getpixel((x - 1, y + 1))[0] * (-2) - \
                      img_source.getpixel((x, y + 1))[0]
            new_px_gf = img_source.getpixel((x, y - 1))[1] + img_source.getpixel((x + 1, y - 1))[1] * (2) - \
                      img_source.getpixel((x - 1, y))[1] + img_source.getpixel((x + 1, y))[1] + \
                      img_source.getpixel((x, y))[1] + img_source.getpixel((x - 1, y + 1))[1] * (-2) - \
                      img_source.getpixel((x, y + 1))[1]
            new_px_bf = img_source.getpixel((x, y - 1))[2] + img_source.getpixel((x + 1, y - 1))[2] * (2) - \
                      img_source.getpixel((x - 1, y))[2] + img_source.getpixel((x + 1, y))[2] + \
                      img_source.getpixel((x, y))[2] + img_source.getpixel((x - 1, y + 1))[2] * (-2) - \
                      img_source.getpixel((x, y + 1))[2]
            img_final_r.putpixel((x, y), (new_px_rf, new_px_gf, new_px_bf))  # Création de la nouvelle image
    save_loca_r = filedialog.asksaveasfilename(initialdir="/", title="Sélectionner un emplacement de sauvegarde",
                                             filetypes=(("Fichier PNG", "*.png"),),
                                             defaultextension='.png')  # Explorateur pour choisir ou sauvegarder la photo
    img_final_r.save(save_loca_r)
    img_final_r.show()  # On montre l'image modifiée


def contraste():  # Effet de contraste
    img_final_co = Image.new('RGB', (largeur, hauteur))
    for x in range(1, largeur - 1):  # On crée une boucle qui prend en charge le nombre de pixel horizontaux
        for y in range(1, hauteur - 1):  # idem mais pour le nbr de pixels verticaux
            px = img_source.getpixel((x, y))
            # Matrice convolution de pixel en 3*3
            new_px_rco = -img_source.getpixel((x, y - 1))[0] - img_source.getpixel((x - 1, y))[0] - \
                       img_source.getpixel((x + 1, y))[0] + img_source.getpixel((x, y))[0] * 5 - \
                       img_source.getpixel((x, y + 1))[0]
            new_px_gco = -img_source.getpixel((x, y - 1))[1] - img_source.getpixel((x - 1, y))[1] - \
                       img_source.getpixel((x + 1, y))[1] + img_source.getpixel((x, y))[1] * 5 - \
                       img_source.getpixel((x, y + 1))[1]
            new_px_bco = -img_source.getpixel((x, y - 1))[2] - img_source.getpixel((x - 1, y))[2] - \
                       img_source.getpixel((x + 1, y))[2] + img_source.getpixel((x, y))[2] * 5 - \
                       img_source.getpixel((x, y + 1))[2]
            img_final_co.putpixel((x, y), (new_px_rco, new_px_gco, new_px_bco))  # Création de la nouvelle image
    save_loca_co = filedialog.asksaveasfilename(initialdir="/", title="Sélectionner un emplacement de sauvegarde",
                                              filetypes=(("Fichier PNG", "*.png"),),
                                              defaultextension='.png')  # Explorateur pour choisir ou sauvegarder la photo
    img_final_co.save(save_loca_co)
    img_final_co.show()  # On montre l'image modifiée


BtnFl = Button(Menu, text='Flouter la photo', command=flou)
BtnFl.pack(side=LEFT, padx=20, pady=5)
BtnCtr = Button(Menu, text='Mettre en avant les contours de la photo', command=contour)
BtnCtr.pack(side=LEFT, padx=10, pady=5)
BtnSp = Button(Menu, text='Choisir une photo', command=lien)
BtnSp.pack(side=LEFT, padx=10, pady=5)
BtnRlf = Button(Menu, text='Ajouter des reliefs à la photo', command=relief)
BtnRlf.pack(side=LEFT, padx=10, pady=5)
BtnCtrst = Button(Menu, text='Changer le contraste de la photo', command=contraste)
BtnCtrst.pack(side=LEFT, padx=10, pady=5)
Menu.resizable(width=False, height=False)
Menu.mainloop()

# © Nitatemic et Matthieu Azzoun Minet
