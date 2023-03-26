import os
import zipfile
import yt_dlp as youtube_dl


def download_audio_or_video(url, output_directory, file_format):
    ydl_opts = {
        'format': 'bestaudio/best' if file_format == 'mp3' else 'bestvideo+bestaudio/best',
        'outtmpl': os.path.join(output_directory, f'%(title)s.{file_format}'),
    }

    if file_format == 'mp3':
        ydl_opts['postprocessors'] = [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            },
            {'key': 'FFmpegMetadata'},
        ]

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        info = ydl.extract_info(url, download=False)
        filename = ydl.prepare_filename(info)
        return filename


def zip_files(files, zip_name, output_directory):
    with zipfile.ZipFile(os.path.join(output_directory, zip_name), 'w') as zipf:
        for file in files:
            zipf.write(file, os.path.basename(file))


def clean_up(files):
    for file in files:
        try:
            os.remove(file)
        except Exception as e:
            print(f"Error removing {file}: {e}")
