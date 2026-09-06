import modules.getinfo as getinfo
import sys
from colorama import Fore, Style, init

init(autoreset=True)

def resume_info(resolution, output): 

    print("-----------------------------------------------------------------")
    print("Qualité de la vidéo : " + Fore.GREEN + f"{resolution}")
    print("Format de la vidéo : " + Fore.GREEN + f"{output}")

    execute = input("Télécharger la vidéo?" + Fore.GREEN + " [Y" + Style.RESET_ALL + " / " + Fore.RED + "N]" + Style.RESET_ALL + " : ")

    if execute == "N":
        print(Fore.RED + "Téléchargement annulé")
        sys.exit()
    


