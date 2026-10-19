

# // Dependencias
# pip install yt-dlp


#!/usr/bin/env python3
"""
Descargador simple de YouTube con yt-dlp
"""

import yt_dlp
import sys

def descargar_youtube(url, tipo='video', carpeta='./descargas'):
    """
    Función simple para descargar videos o audio de YouTube
    
    Args:
        url (str): URL del video
        tipo (str): 'video' o 'audio'
        carpeta (str): Carpeta de destino
    """
    
    # ffmpeg_path = r"C:\Users\guillermorosas_tecno\Videos\Proyectos\ffmpeg-8.0.1-essentials\bin"
    ffmpeg_path = r"C:\Users\guillermorosas_tecno\Videos\Proyectos\Propio\Py_videos\ffmpeg-8.0.1-essentials\bin"

    if tipo == 'video':
        opciones = {
            'outtmpl': f'{carpeta}/%(title)s.%(ext)s',
            'format': 'best[height<=480]',  # Máximo 1080p
            #'format': 'mp4/best',  # Forzar formato MP4

            'writesubtitles': True,
            'writeautomaticsub': True,
            'subtitleslangs': ['en'],
            # 'embedsubtitles': True,

            'extractor_args': {
                'youtube': {
                    'player_client': ['android', 'web']
                }
            },

            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            }
        }
    elif tipo == 'mp3':  # audio
        opciones = {
            'outtmpl': f'{carpeta}/%(title)s.%(ext)s',
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'ffmpeg_location': ffmpeg_path
        }
    
    try:
        with yt_dlp.YoutubeDL(opciones) as ydl:
            ydl.download([url])
        print("✅ Descarga completada!")
        
    except Exception as e:
        print(f"❌ Error: {e}")

# Uso básico
# if __name__ == "__main__":
#     if len(sys.argv) < 2:
#         print("Uso: python descargador.py <URL> [video|audio]")
#         sys.exit(1)
    
#     url = sys.argv[1]
#     tipo = sys.argv[2] if len(sys.argv) > 2 else 'video'
    
#     descargar_youtube(url, tipo)

# YO

# url = "https://www.youtube.com/watch?v=deL5dM9csNc&list=RDdeL5dM9csNc&start_radio=1"
# url = "https://youtu.be/deL5dM9csNc?si=brPqiFacGU30jWN_"
urlHelloween = "https://youtu.be/C5eBZfQW_mg?si=siUG1jNuBRQEXs6m"
url = urlHelloween
print ("Gordoo")
descargar_youtube(url, 'video')
