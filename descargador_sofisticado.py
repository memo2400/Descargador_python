
#!/usr/bin/env python3
"""
Descargador de YouTube usando yt-dlp
Requiere: pip install yt-dlp
"""

import os
import subprocess
import sys
from pathlib import Path

def check_yt_dlp_installed():
    """Verifica si yt-dlp está instalado"""
    try:
        import yt_dlp
        return True
    except ImportError:
        return False

def install_yt_dlp():
    """Instala yt-dlp si no está disponible"""
    print("yt-dlp no está instalado. Instalando...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "yt-dlp"])
        print("✅ yt-dlp instalado correctamente")
        return True
    except subprocess.CalledProcessError:
        print("❌ Error al instalar yt-dlp")
        return False

def download_video(url, download_path="./downloads", quality="best"):
    """
    Descarga un video de YouTube
    
    Args:
        url (str): URL del video de YouTube
        download_path (str): Carpeta donde guardar los archivos
        quality (str): Calidad deseada ('best', 'worst', o formato específico)
    """
    # Crear directorio de descargas si no existe
    Path(download_path).mkdir(exist_ok=True)
    
    # Configuración de yt-dlp
    ydl_opts = {
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'format': quality,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"📥 Descargando: {url}")
            ydl.download([url])
        print("✅ Descarga completada!")
        
    except Exception as e:
        print(f"❌ Error en la descarga: {e}")

def download_audio(url, download_path="./downloads", format="mp3"):
    """
    Descarga solo el audio de un video de YouTube
    
    Args:
        url (str): URL del video de YouTube
        download_path (str): Carpeta donde guardar los archivos
        format (str): Formato de audio ('mp3', 'm4a', 'wav')
    """
    # Crear directorio de descargas si no existe
    Path(download_path).mkdir(exist_ok=True)
    
    # Configuración para extraer audio
    ydl_opts = {
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': format,
            'preferredquality': '192',
        }],
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"🎵 Extrayendo audio: {url}")
            ydl.download([url])
        print("✅ Audio descargado!")
        
    except Exception as e:
        print(f"❌ Error en la descarga de audio: {e}")

def download_playlist(url, download_path="./downloads/playlist"):
    """
    Descarga una playlist completa
    
    Args:
        url (str): URL de la playlist de YouTube
        download_path (str): Carpeta donde guardar los archivos
    """
    Path(download_path).mkdir(exist_ok=True, parents=True)
    
    ydl_opts = {
        'outtmpl': os.path.join(download_path, '%(playlist)s', '%(title)s.%(ext)s'),
        'format': 'best[height<=720]',  # Calidad 720p máximo para playlists
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"📚 Descargando playlist: {url}")
            ydl.download([url])
        print("✅ Playlist descargada!")
        
    except Exception as e:
        print(f"❌ Error descargando playlist: {e}")

def get_video_info(url):
    """Obtiene información del video sin descargarlo"""
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            
            print("\n📊 INFORMACIÓN DEL VIDEO:")
            print(f"Título: {info.get('title', 'N/A')}")
            print(f"Duración: {info.get('duration', 'N/A')} segundos")
            print(f"Autor: {info.get('uploader', 'N/A')}")
            print(f"Vistas: {info.get('view_count', 'N/A')}")
            print(f"URL: {info.get('webpage_url', 'N/A')}")
            
            # Mostrar formatos disponibles
            formats = info.get('formats', [])
            print(f"\n📹 Formatos disponibles: {len(formats)}")
            
    except Exception as e:
        print(f"❌ Error obteniendo información: {e}")

def main():
    """Función principal con menú interactivo"""
    
    # Verificar e instalar yt-dlp si es necesario
    if not check_yt_dlp_installed():
        if not install_yt_dlp():
            return
    
    print("🚀 DESCARGADOR YOUTUBE CON YT-DLP")
    print("=" * 40)
    
    while True:
        print("\n📋 OPCIONES DISPONIBLES:")
        print("1. Descargar video")
        print("2. Descargar solo audio (MP3)")
        print("3. Descargar playlist")
        print("4. Ver información del video")
        print("5. Salir")
        
        opcion = input("\nSelecciona una opción (1-5): ").strip()
        
        if opcion == "5":
            print("👋 ¡Hasta luego!")
            break
            
        url = input("Ingresa la URL de YouTube: ").strip()
        
        if not url:
            print("❌ URL no válida")
            continue
        
        if opcion == "1":
            print("\n🎬 Calidades disponibles:")
            print(" - best: Mejor calidad disponible")
            print(" - worst: Peor calidad")
            print(" - 720p: Video en 720p")
            print(" - 480p: Video en 480p")
            quality = input("Calidad (presiona Enter para 'best'): ").strip() or "best"
            
            download_path = input("Carpeta de descarga (presiona Enter para './downloads'): ").strip() or "./downloads"
            download_video(url, download_path, quality)
            
        elif opcion == "2":
            format_audio = input("Formato de audio (mp3/m4a/wav - presiona Enter para mp3): ").strip() or "mp3"
            download_path = input("Carpeta de descarga (presiona Enter para './downloads'): ").strip() or "./downloads"
            download_audio(url, download_path, format_audio)
            
        elif opcion == "3":
            download_path = input("Carpeta de descarga (presiona Enter para './downloads/playlist'): ").strip() or "./downloads/playlist"
            download_playlist(url, download_path)
            
        elif opcion == "4":
            get_video_info(url)
            
        else:
            print("❌ Opción no válida")

if __name__ == "__main__":
    main()