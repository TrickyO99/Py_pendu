from turtle import*
speed(1)
n=0
for i in range (10) :
    if n==0 :
        forward (100)               #Base
        backward (50)
    if n==1:
        left (90)                   #Potence
        forward (250)
        right (90)
    if n==2 :                       #Planche supérieure
        forward (70)
        right (90)
    if n==3 :
        forward (20)                #Corde
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
        forward (40)                #Bras gauche
        backward (40)
        right (90)
    if n==6 :
        forward (40)                #Bras droit
        backward (40)
        left (45)
    if n==7 :
        forward (70)                #Corps
        left (45)
    if n==8 :
        forward (45)                #Jambe droite
        backward (45)
        right (90)
    if n==9 :
        forward (45)                #Jambe gauche
    n=n+1
mainloop()