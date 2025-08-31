import yt_dlp
import os

def download_youtube_as_mp3(url):
    # Create my_music folder if it doesn't exist
    music_folder = "my_music"
    if not os.path.exists(music_folder):
        os.makedirs(music_folder)
        print(f"Created folder: {music_folder}")
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{music_folder}/%(title)s.%(ext)s',  # Saves file in my_music folder
        'noplaylist': True,              # <--- Only download single video
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',   # High quality
        }],
        'quiet': False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print("Downloading and converting to MP3...")
        ydl.download([url])
        print(f"Done! File saved in {music_folder}/ folder")

if __name__ == "__main__":
    youtube_url = input("Enter a YouTube URL: ").strip()
    download_youtube_as_mp3(youtube_url)
