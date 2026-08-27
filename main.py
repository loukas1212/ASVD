import getinfo
import resumeinfo
import download
from colorama import Fore, Style, init



if __name__ == "__main__": 
    link = input("Merci de rentrer l'URL de la vidéo : ")
    resolution = getinfo.select_resolution()
    output = getinfo.select_format()
    resumeinfo.resume_info(resolution, output)
    download.download_video(link, resolution, output)