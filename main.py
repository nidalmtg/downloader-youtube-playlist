import os
from configparser import ConfigParser
import yt_dlp as youtube_dl
from youtube_converter import download_audio_or_video, zip_files, clean_up


def main():
    config = ConfigParser()
    config.read("config.ini")

    playlist_link = config.get("Settings", "playlist_link")
    output_directory = config.get("Settings", "output_directory")
    file_format = config.get("Settings", "file_format")

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    ydl_opts = {
        "extract_flat": True,
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(playlist_link, download=False)
        playlist_title = info.get("title", "Untitled Playlist")
        video_urls = [entry["url"] for entry in info["entries"] if entry["url"]]

    print(f"Downloading playlist: {playlist_title}")

    media_files = []

    for url in video_urls:
        try:
            print(f"Downloading: {url}")
            media_path = download_audio_or_video(url, output_directory, file_format)
            media_files.append(media_path)
        except Exception as e:
            print(f"Error downloading {url}: {e}")

    zip_name = f"{playlist_title}.zip"
    zip_files(media_files, zip_name, output_directory)
    print(f"Playlist saved as {zip_name}")


if __name__ == "__main__":
    main()
