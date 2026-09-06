import colorama
from colorama import Fore, Style, init

init(autoreset=True)

def select_resolution():
    print("---------------------------------------------------------------------------")
    print("1 - 144p")
    print("2 - 240p")
    print("3 - 360p")
    print("4 - 480p")
    print("5 - 720p")
    print("6 - 1080p")
    print("7 - 1444p (2k)")
    print("8 - 2160 (4k)")
    choice = input("Merci de choisir la résolution souhaitée (1, 2, 3, 4, 5, 6, 7, 8) : ")

    if choice == "1":
        return "144"
    elif choice == "2":
        return "240"
    elif choice == "3":
        return "360"
    elif choice == "4":
        return "480"
    elif choice == "5":
        return "720"
    elif choice == "6":
        return "1080"
    elif choice == "7":
        return "1444"
    elif choice == "8":
        return "2160"
    else:
        print(Fore.RED + "!!! Choix invalide, qualité par défaut sélectionnée (480p) !!!")
        return "480"
    
def select_format():
    print("---------------------------------------------------------------------------")
    print("1 - .mp4")
    print("2 - .mkv")
    print("3 - .webm")
    choice = input("Merci de choisir le format souhaité (1, 2, 3) : ")

    if choice == "1":
        return "mp4"
    elif choice == "2":
        return "mkv"
    elif choice == "3":
        return "webm"
    else:
        print(Fore.RED + "!!! Choix invalide, format par défaut sélectionné (mp4) !!!")
        return "mp4"
