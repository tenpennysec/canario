# Autor: tenpenny
import yt_dlp
import click

@click.group()
def cli():
    pass

@click.command()
@click.argument('link')
@click.option('--keep_video', is_flag=True, help='Pass this to keep the video')
def download_audio(link, keep_video):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'ffmpeg-location': './',
        'outtmpl': "./%(id)s.%(ext)s",
        'keepvideo': keep_video
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

cli.add_command(download_audio)

if __name__ == "__main__":
    cli()
