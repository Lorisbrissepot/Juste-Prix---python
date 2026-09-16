# Créé par GGast, le 20/04/2026 en Python 3.7
import random
# menu

jouer = True # la valeur jouer est True, elle va permettre au proggrame de lancer le jeu ou pas
while jouer == True: # tant que la valeur jouer est True, le proggramme va lancer le jeu
    retour = True  # la valeur retour est True, elle pemettra de relancer le proggramme depuis le debut si l'option retour est choisi
    while retour == True: # Tant que la valeur retour sera True le début du proggramme ce relancera
        error = True # la valeur error est True, elle va permettre de bloqué les action pas prévue par le programme et éviter que ce dernier ce termine au mauvais moment
        while error == True: # tant que la valeur error est True il execute en boucle la partie menu du proggramme
            print ("Bienvenue sur le JUSTE PRIX.") # Le proggramme sort du texte pour expliquer le jeu
            print ("Voici les règles: Le proggramme choisi une valeur aléatoire entre 10 000 et 1 000 000 . Votre but est de trouver la valeur généré aléatoirement, pour cela vous avez un certains nombre de proposition, a chaque proposition le programme vous renvoie si vous êtes en dessous ou au dessus de la valeur recherché. Si vous n'avez plus de proposition disponible vous avez perdu.")
            print ("Choissisez votre mode de jeu en entrant dans la console 1 ou 2:")
            print (" 1. jeu solo")
            print (" 2. jeu a deux")
            modejeu = int(input()) # ici l'utilisateur entre 1 ou 2 pour sélectionner son mode de jeu
            if modejeu == 1 or modejeu == 2: # si l'utilisateur à entré 1 ou 2 plus tôt alors la variable error prend la valeur False et permet de sortir de la boucle while car il n'y a pas d'erreur
                error = False
            else:
                print("Cette option n'existe pas.") # si l'utilisateur à entré un valeur différente de 1 ou 2 alors error reste True  signifiant qu'il y a une erreur, le proggramme reéxécute la partie menu du proggrame en indiquant l'erreur


        # parametres du jeu
        error = True # la valeur error redevient True
        while error == True: # tant que la valeur error est True le proggramme executeras en boucle
            if modejeu == 1:  # Si l'utilisateur un rentrer 1 plutot le programme indique qu'il a sélectionné le mode solo
                print(" Vous avez sélectionner le mode solo. Veuiller maintenant sélectionné la difficulté: ")
            else: # Si l'utilisateur a choisi autre chose que 1 (c'est a dire 2 car les autres choix bloque le proggramme) il indique qu'il a sélectionné le mode duo
                print(" Vous avez sélectionner le mode duo. Veuiller maintenant sélectionné la difficulté: ") # Le proggramme sort du texte pour proposé les différentes difficulté
            print (" 1. facile (40 prposition)")
            print (" 2. moyen (20 proposition)")
            print (" 3. difficile (10 proposition)")
            print (" 4. retour")
            difficulte = int(input()) # l'utilisateur peut rentrer 1, 2 ou 3 pour sélectionner le mode de difficulté
            if modejeu <= 4 and modejeu >= 1: # Si l'utilisateur a rentrer 1, 2 ou 3 plutot la variable error devient False et permet a la suite du proggramme de s'éxécuter
                error = False
            else:   # Si l'utilisateur rentre autre chose que 1, 2 ou 3 il renvoie un message d'erreur et redemande un choix de difficulté
                print("Cette option n'existe pas.")

            if difficulte == 1: # Si l'utilisateur a rentrer 1 dans la console plus tot alors la variable nbproposition prend la valeur 40
                nbproposition = 40
                retour = False # error devient False et permet de sortir de la boucle et de démarrer le jeu avec les paramètre choisi
            elif difficulte == 2: # Si l'utilisateur a rentrer 2 dans la console plus tot alors la variable nbproposition prend la valeur 20
                nbproposition = 20
                retour = False # error devient False et permet de sortir de la boucle et de démarrer le jeu avec les paramètre choisi
            elif difficulte == 3: # Si l'utilisateur a rentrer 3 dans la console plus tot alors la variable nbproposition prend la valeur 10
                nbproposition = 10
                retour = False # error devient False et permet de sortir de la boucle et de démarrer le jeu avec les paramètre choisi

    #jeu solo et duo
    if modejeu == 1: # Si le joueur a choisi le mode solo en rentrant 1 dans la variable modejeu le proggrame donne a la variable bonprix (la valeur a trouvé pour gagner le jeu) une valeur aléatoire entre 10000 et 1000000
        bonprix = random.randint(10000,1000000)
    else: # Dans l'autre cas (si le joueurs a choisi le mode duo en rentrant 2 dans la variable modejeu alors le proggramme sort du texte pour expliquer que le joueurs deux doit rentrer la valeur que le joueurs 1 devra trouver. Puis il va stosker cette valeur dans la variable bonprix
        print("Premier joueur choissez la valeur que le deuxième joueur doit trouver")
        bonprix = int(input())       # Pour le mode duo c'est la valeur a trouver
    propositionactuelle = 0      # Création de la variable propositionactuelle qui permet de compter le nombre de proposition utiliser (pour le moment elle est égale a 0)
    essais = -1                 # création de la variable essais
    print(" ET C'EST PARTI")     # Le proggramme sort du texte pour annoncer le démarrage du jeu

     #jeu
    while propositionactuelle != nbproposition and essais != bonprix: #le proggramme continue a tourné tant qu'il reste des propositions ou tant que le bon prix n'a pas été trouvé
        print("nombre de propositions restante", nbproposition - propositionactuelle) # Le proggramme sort un texte qui indique le nombre de propositions restantes
        propositionactuelle = propositionactuelle + 1 #permet au proggramme de compter combien de proposition ont été utilisé
        essais = int(input())  # cette partie du proggramme lit et test la réponse du joueur
        if essais < bonprix: # Si la réponse donnée est en dessous de la bonne réponse le proggramme indique que la bonne valeur est plus haute
            print("C'est plus")
        elif essais > bonprix: # Si la réponse donnée est au dessus de la bonne réponse le proggramme indique que la bonne valeur est plus basse
            print("C'est moins")
        else: # Si la réponse donné au proggramme est la même que la valeur du bon prix alors le proggramme sort un message de félicitation
            print("AH OUI OUI OUI C'EST GAGNÉ")
    if essais != bonprix: # Si en sortant de la boucle while, la dernière valeur proposé est différente de la variable bon prix alors le proggramme sort un message pour indiquer au joueurs qu'il a perdu
        print ("C'est perdu, la bonne réponse était", bonprix)


    # rejouer
    error = True # la variable error devient True
    while error == True: # Tant que error sera True la partie rejouer du proggramme va se relancer en boucle
        print ("Voulez vous rejouer") # Le proggramme sort du texte pour proposer de rejouer
        print ("1. OUI")
        print ("2. NON")
        rejouer = int(input()) # Le proggramme demande la réponse de l'utilisateur (1 ou 2) a la question précédente
        if rejouer == 2: # Si l'utilisateur à rentrer 2 alors la variable jouer devient False et permet de sortir de la boucle et terminer le proggramme sinon la variable reste vrai et le jeu se relance
            jouer = False
        if rejouer == 1 or rejouer == 2: # si l'utilisateur à entré 1 ou 2 plus tôt alors la variable error prend la valeur False et permet de sortir de la boucle while car il n'y a pas d'erreur
            error = False
        else:
            print("Cette option n'existe pas.") # si l'utilisateur à entré un valeur différente de 1 ou 2 alors error reste True  signifiant qu'il y a une erreur, le proggramme reéxécute la partie menu du proggrame en indiquant l'erreur











