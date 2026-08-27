import yt_dlp
from colorama import Fore, Style, init

def download_video(url, resolution, output):
    options = {
        'format': f'bestvideo[height<={resolution}]+bestaudio/best[height<={resolution}]',
        'merge_output_format': output,
        'outtmp1': '%(title)s%(ext)s',
        'quiet': True,
        'no_warnings': True,
    }

    try:
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])
        print(Fore.GREEN + "Téléchargement réussi" + Style.RESET_ALL)
    except Exception as error:
        print(Fore.RED + f"!!! Téléchargement échoué, erreur : {error} !!!" + Style.RESET_ALL)