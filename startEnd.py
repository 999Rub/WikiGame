from bs4 import BeautifulSoup
import urllib.request
import tkinter
import tkinter.messagebox

# Fonction de création d'un url aléatoire via wikipédia
def createNav(url):
    with urllib.request.urlopen(url) as response:
        webpage = response.read()
        soup = BeautifulSoup(webpage, 'html.parser')
    return soup


# url random de base 
url = 'https://fr.wikipedia.org/wiki/Special:Random/Article'
# page de départ créée aléatoirement
start = createNav(url)
# idem pour la page d'arrivée
end = createNav(url)

    

