import yt_dlp
from tqdm import tqdm
from colorama import Fore, Style, init


def download_video(url, resolution, output):
    pbar = None

    def hook(d):
        nonlocal pbar

        if d['status'] == 'downloading':
            total = d.get('total_bytes') or d.get('total_bytes_estimate')
            downloaded = d.get('downloaded_bytes', 0)

            if pbar is None and total:
                pbar = tqdm(
                    total=total,
                    unit='B',
                    unit_scale=True,
                    unit_divisor=1024,
                    desc="Téléchargement",
                    ascii="-#"
                )

            if pbar is not None:
                pbar.n = downloaded
                pbar.refresh()

        elif d['status'] == 'finished':
            if pbar is not None: 
                pbar.close()
                pbar = None

    options = {
        'format': f'bestvideo[height<={resolution}]+bestaudio/best[height<={resolution}]',
        'merge_output_format': output,
        'outtmpl': '%(title)s.%(ext)s',
        'quiet': True,
        'no_warnings': True,
        'progress_hooks': [hook],
    }

    try:
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])
        print(Fore.GREEN + "Téléchargement réussi" + Style.RESET_ALL)
    except Exception as error:
        print(Fore.RED + f"!!! Téléchargement échoué, erreur : {error} !!!" + Style.RESET_ALL)