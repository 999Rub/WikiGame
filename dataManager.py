from bs4 import BeautifulSoup
from startEnd import createNav
import urllib.request
import tkinter
import tkinter.messagebox
import startEnd

endroot = startEnd.end
# instanciation de tkinter
top = tkinter.Tk()
widget = tkinter.Listbox(top, width=100, height=100)
widgetTitre = tkinter.messagebox.Message(top)
menubar = tkinter.Menu(top)
top.config(menu=menubar) 
menufichier = tkinter.Menu(menubar,tearoff=0)
menuHistorique = tkinter.Menu(menubar,tearoff=0)
top.title("WikiGame (double cliquer pour charger une autre page)")
top.configure(background="#ebe2cc")

# deux list pour save temporairement les ancres / titres
ancorlist = []
titlelist = []


# lists qui savent jusque la fermeture du jeu les titres et ancres de pages cliqués uniquement
HistoriqueAncor = []
HistoriqueTitle = []


# fonction principal qui créer la fenetre tkinter avec tout le jeu, instancian toutes les autres fonctions
def viewData(root, currentroot,  endroot):
    # rafraichissement de la fenetre tkinter à chaque création
    menubar.delete(0, 'end')
    menuHistorique.delete(0,'end')
    widget.delete(0, 'end')
    startData( root,currentroot)
    endData(endroot)
    # rafraichissement des listes contenant les ancres et les titre
    ancorlist.clear()
    titlelist.clear()

    # scrapping de la page wikipédia
    for te in currentroot.findAll("div", {"class": "mw-content-ltr"}):
        for child in te.findChildren("a"):
            if (child.get("title") !=  None):
                if  ":" not in child.get("href") and "Modifier" not in child.get("title"):
                    ancorlist.append(child.get("href"))
                    titlelist.append(child.get("title"))
    # affichage du scrapping      
    for i in range(len(titlelist)) :
        widget.insert('end', titlelist[i])
    widget.bind('<Double-1>', go)  
    # ici on charge le menu historique à nouveau pour le mettre à jour  
    if (HistoriqueTitle):
        menubar.add_cascade(label="Historique : "+ HistoriqueTitle[len(HistoriqueTitle)-2], menu=menuHistorique)
        for y in range(len(HistoriqueTitle)):
            menuHistorique.add_command(label= str(y+1) + " " + HistoriqueTitle[y]) 
    top.geometry("1000x500")
    widget.pack() 
    top.mainloop()
    

    
# fonction qui affiche la page de départ et actuelle via le scrapping
def startData(root, currentroot):
    curroot = ''
    # premier scrapping pour conserver le titre de la page de départ
    for ye in root.findAll("h1", {"id":"firstHeading"}):
        menubar.add_cascade(label="Page de départ : "+ ye.getText(), menu=menufichier) 
        ye.find("h1", {"id":"firstHeading"})
    # deuxieme scrapping ce coup ci sur la page actuelle
    for ya in currentroot.findAll("h1", {"id":"firstHeading"}):
        menubar.add_cascade(label="Page actuelle : "+ ya.getText(), menu=menufichier) 
        curroot = ya.getText()

    return curroot


# affiche la page d'arrivée via le scrapping de la page
def endData(endroot):
    endrootReturn = ''
    for ye in endroot.findAll("h1", {"id":"firstHeading"}):
        menubar.add_cascade(label="Page d'arrivée : "+ ye.getText(), menu=menufichier) 
        endrootReturn = ye.getText()
        ye.find("h1", {"id":"firstHeading"})
    return endrootReturn

# update de la fenetre en rechargent une nouvelle list contenant les nouvelles pages / données
def refresh(self,  root, currentroot, endroot):
    viewData(root, currentroot,  endroot)
    self.update()

# detection de l'arrivée sur la page finale
def win(self, currentroot, endroot):
    ct=+1
    if startData(startEnd.start, currentroot) == endData(endroot):
        print("Bravo vous avez gagné en "+ str(ct)+ " coups")
        self.destroy()

# fonction contenant l'historique des pages vues (cliquer sur le menu historique pour afficher toutes les pages vues)
def back(cs):
    HistoriqueAncor.append(ancorlist[cs[0]])
    HistoriqueTitle.append(titlelist[cs[0]])


# fonction au double click  d'un titre de page va charger la nouvelle page avec toutes les nouvelles données à jour
def go(event): 
    cs = widget.curselection()     
    url = "https://fr.wikipedia.org"+ancorlist[cs[0]]
    # root récupère le lien cliqué et charge la page correspondante
    currentroot = createNav(url)
    back(cs)
    refresh(top,   startEnd.start, currentroot, endroot)
    win(top, currentroot, endroot)