def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    jour, heure, minute, seconde = temps
    return ((jour*24 + heure)*60 + minute)*60 + seconde


temps = (3, 23, 1, 34)
print(type(temps))
print(tempsEnSeconde(temps))


def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    jour = seconde // (24*60*60)
    seconde = seconde % (24*60*60)
    heure = seconde // (60 * 60)
    seconde = seconde % (60*60)
    minute = seconde // 60
    seconde = seconde % 60
    return (jour, heure, minute, seconde)


temps = secondeEnTemps(100000)
print(temps[0], "jours", temps[1], "heures", temps[2], "minutes", temps[3], "secondes")


# fonction auxiliaire ici

def affiche_pluriel(valeur, mot):
    if(valeur != 0):
        print(valeur, "", end="")
        print(mot, end="")
        if(valeur > 1):
            print("s", end="")
        print(" ", end="")


def afficheTemps(temps):
    affiche_pluriel(temps[0], "jour")
    affiche_pluriel(temps[1], "heure")
    affiche_pluriel(temps[2], "minute")
    affiche_pluriel(temps[3], "seconde")
    print()


afficheTemps((1, 0, 14, 23))


def demandeTemps():
    jour = int(input("Entrer un nombre de jours"))
    heure = int(input("Entrer un nombre d'heures"))
    if(heure > 23):
        print("Nombre d'heures incorrect")
        return
    minute = int(input("Entrer un nombre de minutes"))
    if(minute > 59):
        print("Nombre de minutes incorrect")
        return
    seconde = int(input("Entrer un nombre de secondes"))
    if(seconde > 59):
        print("Nombre de secondes incorrect")
        return
    return (jour, heure, minute, seconde)


#afficheTemps(demandeTemps())


def sommeTemps(temps1, temps2):
    return secondeEnTemps(tempsEnSeconde(temps1) + tempsEnSeconde(temps2))


afficheTemps(sommeTemps((2, 3, 4, 25), (5, 22, 57, 1)))

def proportionTemps(temps,proportion):
    pass
afficheTemps(proportionTemps((2,0,36,0),0.2))
#appeler la fonction en échangeant l'ordre des arguments