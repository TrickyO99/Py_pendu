from turtle import*
import random

speed (1)
n=0

ficher = open("Bibliotheque.txt", "r")
liste_lignes = ficher.readlines()
liste_mots_jouables = []

for ligne in liste_lignes :
    liste_mots_jouables.append(ligne)

z = random.randint(0, len(liste_mots_jouables) - 1)
motatrouver = liste_mots_jouables[z]
motatrouver = "".join(motatrouver)

Nombre_de_chances = 10
Username = input("Entrez votre nom d'utilisateur")
while len(Username)<4 :
    Username = input("Votre nom d'utilisateur est trop court, c'est 4 lettres minimum")
lettres_used = []
tirets = ["-","-","-","-","-","-","-","-"]

print ("        LE JEU DU PENDU")
print ("     Version définitive")
print ("TRIKI Othmane & BENKHEMIS David")
print ("Attention, la difficultée est extrème (62000 mots !)")
print ("Règles: :Si vous n'avez plus de chances disponibles, vous perdez.")
print ("         Si vous trouvez le mot tandis qu'il vous reste des chances, vous gagnez")
print ("         Vous perdez une chance à chaque lettre saisie qui n'est pas dans le mot, alors faites attention.")

while Nombre_de_chances > 0 :

    if ("-".join(tirets)) != ("-".join(motatrouver[1:9])) :

        print("Il vous reste ", Nombre_de_chances, "essais.")
        print("Vous avez déjà utilisé les lettres :", ",".join(lettres_used))
        for i in range (8) :
            if motatrouver[0] == motatrouver[i+1] :
                tirets[i]=motatrouver[0]
            if motatrouver[9] == motatrouver[i+1] :
                tirets[i]=motatrouver[9]
        print("Votre avancement :",motatrouver[0]," ".join(tirets), motatrouver[9])
        print("___________________________________________________________________")

        lettre = input("Saisissez une lettre")
        while len(lettre) > 1 :
                lettre = input("Saisissez UNE lettre, svp")
        lettre = lettre.upper()

        if lettre in lettres_used :
            print ("Vous avez déjà utilisé cette lettre")
            Nombre_de_chances = Nombre_de_chances - 1
        else :
            lettres_used.append(lettre)
            Nombre_de_chances = Nombre_de_chances - 1

        if lettre in motatrouver :

            Nombre_de_chances = Nombre_de_chances + 1
            for y in range (8) :
                if lettre == motatrouver[y+1] :
                    tirets[y] = lettre

        elif lettre in lettres_used :

            if n==0 :
                forward (100)
                backward (50)
            if n==1:
                left (90)
                forward (250)
                right (90)
            if n==2 :
                forward (70)
                right (90)
            if n==3 :
                forward (20)
                penup()
                forward (30)
                pendown()
                left (90)
            if n==4 :
                speed(100)
                compteur = 0
                while compteur < 180 :
                    forward (0.50)
                    left (2)
                    compteur = compteur + 1
                right (45)
                speed(1)
            if n==5 :
                forward (40)
                backward (40)
                right (90)
            if n==6 :
                forward (40)
                backward (40)
                left (45)
            if n==7 :
                forward (70)
                left (45)
            if n==8 :
                forward (45)
                backward (45)
                right (90)
            if n==9 :
                forward (45)
            n=abs(Nombre_de_chances-10)

        else :

            if n==0 :
                forward (100)
                backward (50)
            if n==1:
                left (90)
                forward (250)
                right (90)
            if n==2 :
                forward (70)
                right (90)
            if n==3 :
                forward (20)
                penup()
                forward (30)
                pendown()
                left (90)
            if n==4 :
                speed(100)
                compteur = 0
                while compteur < 180 :
                    forward (0.50)
                    left (2)
                    compteur = compteur + 1
                right (45)
                speed(1)
            if n==5 :
                forward (40)
                backward (40)
                right (90)
            if n==6 :
                forward (40)
                backward (40)
                left (45)
            if n==7 :
                forward (70)
                left (45)
            if n==8 :
                forward (45)
                backward (45)
                right (90)
            if n==9 :
                forward (45)
            n=abs(Nombre_de_chances-10)

    if ("-".join(tirets)) == ("-".join(motatrouver[1:9])) :
        Nombre_de_chances = 0                                 #Sert à sortir de la boucle

if ("-".join(tirets)) == ("-".join(motatrouver[1:9])) :       #WIN
    print ("Félicitations",Username,"vous avez gagné !!")
    print ("Le mot était :", motatrouver)
    print ("Félicitations !!")

else :
    print (Username, "vous avez perdu ...")                   #LOSE
    print ("Dommage, réessayez !")
    print ("Le mot était :", motatrouver)

mainloop()