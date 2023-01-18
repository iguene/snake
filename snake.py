from upemtk import *
from time import sleep
from random import*
# dimensions du jeu
taille_case = 15
largeur_plateau = 40  # en nombre de cases
hauteur_plateau = 30  # en nombre de cases
c=0

def case_vers_pixel(case):
    """
    Fonction recevant les coordonnées d'une case du plateau sous la forme
    d'un couple d'entiers (ligne, colonne) et renvoyant les coordonnées du
    pixel se trouvant au centre de cette case. Ce calcul prend en compte la
    taille de chaque case, donnée par la variable globale taille_case.  
    """
    i, j = case
    return (i + .5) * taille_case, (j + .5) * taille_case


def affiche_pommes(pommes):
    for p in pommes:
       x, y = case_vers_pixel(p)
       cercle(x, y, taille_case/2,
           couleur='darkred', remplissage='red')
       rectangle(x-2, y-taille_case*.4, x+2, y-taille_case*.7,
              couleur='darkgreen', remplissage='darkgreen')


def affiche_serpent(serpent):
    for i in serpent:
        x, y = case_vers_pixel(i)  # à modifier !!!

        cercle(x, y, taille_case/2 + 1,
               couleur='darkgreen', remplissage='green')



def bords(serpent):
    x,y= serpent[0]
    if x<0:
        x=40
    elif x>40:
        x=0
    elif y<0:
        y=30
    elif y>30:
        y=0
    serpent[0]=(x,y)

def change_direction(direction, touche):
    # à compléter !!!
    if touche == 'Up':
        # flèche haut pressée
        return (0, -1)
    elif touche == 'Down':
        return (0, 1)
    elif touche == "Left":
        return (-1, 0)
    elif  touche == "Right":
        return (1,0 )
    else:
        # pas de changement !
        return direction

def deplace_serpent(serpent,direction):
    head=serpent[0]
    new_head=[head[0]+direction[0],head[1]+direction[1]]
    serpent.insert(0,new_head)
    serpent.pop()
   
def creer_pommes(n):
    pommes = []
    while n > 0:
        pos1=randint(0,39)
        pos2=randint(0,29)
        pommes.append([pos1,pos2])
        n -= 1
    return pommes

def contains(couple, lst):
    l = [couple[0], couple[1]]
    for elem in lst:
        if elem == l:
            return True
    return False

def serpent_mange_pomme(serpent, pommes,c):
    head=serpent[0]
    element = [head[0],head[1]]
    while contains(element, pommes) == True :
       pommes.remove(element)
       serpent.append(element)
       pommes.append([randint(0,39),randint(0,29)])
       c+=1
       
    return pommes
print('votre score est de ',c)
# programme principal
if __name__ == "__main__":
    # initialisation du jeu
    pommes = creer_pommes(1)
    framerate = 10    # taux de rafraîchissement du jeu en images/s
    serpent = [[1, 1]]
    
    direction = (0, 0)  # direction initiale du serpent
    cree_fenetre(taille_case * largeur_plateau,
                 taille_case * hauteur_plateau)
  

    # boucle principale
    while True:
        # affichage des objets
        efface_tout()
        affiche_pommes(pommes)   # à modifier !       
        affiche_serpent(serpent)  # à modifier !
        mise_a_jour()
    
        # gestion des événements
        ev = donne_evenement()
        ty = type_evenement(ev)
        if ty == 'Quitte':
            break
        elif ty == 'Touche':
            print(touche(ev))
            direction = change_direction(direction, touche(ev))

        deplace_serpent(serpent, direction)
        serpent_mange_pomme(serpent,pommes,c)
        bords(serpent)
        # attente avant rafraîchissement
        sleep(1/framerate)
   
    # fermeture et sortie
    ferme_fenetre()
