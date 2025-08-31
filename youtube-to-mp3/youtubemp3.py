import yt_dlp

def download_youtube_as_mp3(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',  # Saves file as video_title.mp3
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
        print("Done!")

if __name__ == "__main__":
    youtube_url = input("Enter a YouTube URL: ").strip()
    download_youtube_as_mp3(youtube_url)
