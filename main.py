import os
from configparser import ConfigParser
from pytube import Playlist
from youtube_converter import download_audio_or_video, zip_files


def main():
    config = ConfigParser()
    config.read("config.ini")

    playlist_link = config.get("Settings", "playlist_link")
    output_directory = config.get("Settings", "output_directory")
    file_format = config.get("Settings", "file_format")

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    playlist = Playlist(playlist_link)
    print(f"Downloading playlist: {playlist.title}")

    media_files = []

    for url in playlist.video_urls:
        try:
            print(f"Downloading: {url}")
            media_path = download_audio_or_video(url, output_directory, file_format)
            media_files.append(media_path)
        except Exception as e:
            print(f"Error downloading {url}: {e}")

    zip_name = f"{playlist.title}.zip"
    zip_files(media_files, zip_name, output_directory)
    print(f"Playlist saved as {zip_name}")


if __name__ == "__main__":
    main()
