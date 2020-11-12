n = int(input("Entrer votre entier"))

if n > 25 and n < 50:
    print("Gagné")
else: 
    print("Dommage")

#afficher n fois aaaa....aaaab  avec n a dans l'expression aaaa...aaab

n = 10
for i in range(n):
    print("a"*n+"b")

#afficher combien de fois il faut diviser n par 3 pour passer en dessous de 1
n = 10 ** 5
tour_boucle = 0
while n >= 1:
    n = n/3
    tour_boucle = tour_boucle + 1
print(tour_boucle)