from pytube import YouTube, streams
from pytube.cli import on_progress

link = str(input("insira um link: "))

yt = YouTube(link, on_progress_callback = on_progress)

print(f"Título = {yt.title}")

print("baixando...")

ys = yt.streams.get_highest_resolution()
ys.download()