from bs4 import BeautifulSoup
import startEnd
import urllib.request
import tkinter
import tkinter.messagebox
from dataManager import viewData


# on récupère le start root et le end root généré aléatoirement depuis le fichier startEnd
start = startEnd.start
end = startEnd.end



# on instancie la fonction principal qui va afficher les données et plus gobalemment le jeu
viewData(start, start , end)