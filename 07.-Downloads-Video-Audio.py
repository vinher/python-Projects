#Fecha:22-10-21
#Descripción: Srcipt para descargar video y audio de you tube con python y pytube
#Para ejecutar este script debes instalar pytube.
#Se instala con el comando pip install pytube
#Con esto ya puedes ejecutar el Script para descargar audio y video de you tube

#Importamos la librería pytube
import pytube




#Creamos un menú sencillo
print("DESCARGA VIDEOS Y AUDIOS")
print("1.-Descargar Video: ")
print("2.-Descargar Audio: ")

#Creamos una función en python para poder descargar videos o audios
def download():
    op = int(input("Ingrese el numero de la opción: "))
    if op == 1:
        var = input("Ingrese el link del video: ")
        yt = pytube.YouTube(var)
        path = "/home/vinher/Downloads"
        yt.streams.first().download(path)
        print("\n","Descarga Éxitosa Archivo Guardado En: ","\n",path, "\n","Con el Nombre: ", yt.title)
        opcion()
    elif op == 2:
        var = input("Ingrese el link del video: ")
        path="/home/vinher/Downloads"
        yt = pytube.YouTube(var)
        #El numero 140 indica el tag, un tag indica el formato del archivo en este caso el formato 140
        #representa el formato mp4
        st=yt.streams.get_by_itag("140")#251
        st.download(path)

        print("\n","Descarga Éxitosa Archivo Guardado En: ","\n",path, "\n","Con el Nombre: ", yt.title)

        opcion()
    else:
        print("Ingrese una opción valida ")
        download()

def opcion():
    op = input("Descargar otro archivo Si/No: ")
    if op == 'Si' or op == 'si':
        download()
    elif op == 'No' or op == 'no':
        print("Programa Finalizado")
    else:
        print("Ingrese una opción correcta")
        download()
download()
