#Para ejecutar este script debes tener instalado
#pytube y tqdm
#Instalación de pytube: pip install pytube
#Instalación de tqdm: pip install tqdm

from pytube import Playlist
from tqdm import tqdm

var = input("Ingrese el link de la playlist: ")

playlist = Playlist(var)
print(f'Titulo: {playlist.title}')

loop = tqdm(total = len(playlist), position=0, leave = False)
for video in playlist.videos:
    loop.set_description("Downloading...".format(video))
    video.streams.first().download()
    loop.update(1)
loop.close()


print("Descarga Exitosa")
