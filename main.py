import argparse
import modules.getinfo as getinfo
import modules.resumeinfo as resumeinfo
import modules.download as download
from colorama import Fore, Style, init

def parse_args():
    parser = argparse.ArgumentParser(description="ASVD")
    parser.add_argument(
        "-u", "--url",
        type=str,
        default=None,
        help="URL de la vidéo à télécharger"
    )
    parser.add_argument(
        "-r", "--resolution",
        type=str,
        default=None,
        choices=["144", "240", "360", "480", "720", "1080", "1444", "2160"],
        help="Résolution souhaitée (144, 240, 360, 480, 720, 1080, 1444, 2160)"
    )
    parser.add_argument(
        "-f", "--format",
        type=str,
        default=None,
        choices=["mp4", 'mkv', "webm"],
        help="Format de sortie"
    )
    return parser.parse_args()

if __name__ == "__main__": 
    args= parse_args()

    link = args.url if args.url else input("Merci de rentrer l'URL de la vidéo : ")
    resolution = args.resolution if args.resolution else getinfo.select_resolution()
    output = args.format if args.format else getinfo.select_format()

    resumeinfo.resume_info(resolution, output)
    download.download_video(link, resolution, output)