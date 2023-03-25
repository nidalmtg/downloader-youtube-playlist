# YouTube Playlist Converter
This Python application allows you to download a YouTube playlist and convert it to MP3 format. It uses the <code>yt_dlp</code> and <code>pytube</code> libraries to download the videos and <code>ffmpeg</code> to convert them to MP3 format.

## Prerequisites
Before using this application, make sure you have <code>ffmpeg</code> installed on your system.

## Installation
To install and use the application, follow these steps:
<li>Clone the repository or download the source code.</p></li><li>Install the required libraries by running the following command:</li>

```python
pip install -r requirements.txt
```

</code></div></div></pre><p>This will install the <code>yt_dlp</code> and <code>pytube</code> libraries.</p></li><li>Create a <code>config.ini</code> file in the root directory of the project with the following content:</p>

```python
[Settings]
playlist_link = https://www.youtube.com/playlist?list=PLAYLIST_URL
output_directory = /path/to/output/directory
file_format = mp3
```

</code></div></div></pre><p>Replace <code>PLAYLIST_URL</code> with the URL of the YouTube playlist you want to download, and <code>/path/to/output/directory</code> with the path to the directory where you want to save the converted MP3 files.</p></li>
## Usage
To use this application, run the following command:
```python
python main.py
```
This will download all the videos in the playlist, convert them to MP3 format (or MP4 if you changed the file_format parameter in the config.ini file), and save them in a zip file in the specified output directory.

## Notes
<li>If you encounter any errors while running the application, please make sure that you have a stable internet connection and that the YouTube videos are available in your region.
<li>The application may take some time to download and convert large playlists. Please be patient and wait for the process to finish.