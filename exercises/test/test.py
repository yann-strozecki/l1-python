print("helloword")


def crypte(chaine, cle):
    """ Retourne une chaîne de caractères cryptée en décalant chaque lettre de chaine par l'entier cle"""
    res = ""
    for i in range(len(chaine)):
        res += chr(ord(chaine[i]) + cle)
    return res


message_crypte = crypte(input(), 1)
print(message_crypte)
message_decrypte = crypte(message_crypte, -1)
print(message_decrypte)
