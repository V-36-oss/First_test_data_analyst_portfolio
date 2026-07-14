from colorama import Fore, Back, Style,init

#This part shows the name of the author
print(Fore.CYAN + "*-"*20)
print(Fore.CYAN + "Author: Christophe Coovi VAGNONNOUKESSE")
print(Fore.CYAN + "*-"*20)
print()

 #This part shows the text in colour
init()# important pour windows
print(Fore.RED + "Ceci est en ROUGE")
print(Fore.GREEN + "Ceci est en VERT")
print(Fore.BLUE + "Ceci est en BLEU")
print(Back.BLUE + Fore.BLACK + "Fond JAUNE,texte NOIR")
print(Style.RESET_ALL + "Et là on revient à la normale") #Remets tout à zéro +le texte
#Fore=Couleur du texte
#Back=Couleur du fond
# Style=Gras,Normal,etc
#init() =active colorama pour windows