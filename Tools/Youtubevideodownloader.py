from pytube import YouTube
from os import getcwd,path,sys


def info(data):
    print('='*50)
    print(f'Title : {data.title}')
    print(f'Channel name : {data.author}')
    length = data.length
    print(f'Length : {length//60} min {length%60} sec')
    print(f'Age restricted : {data.age_restricted}')
    print(f'Rating : {round(data.rating,1)}/5')
    print(f'Views : {data.views}')
    print('Description :-')
    print(data.description)
    print('='*50,'\n')

def progress_func(stream,chunk,bytes_remaining):
    curr = stream.filesize - bytes_remaining
    done = int(50 * curr / stream.filesize)
    sys.stdout.write(f"\r[{'=' * done}{' ' * (50-done)}{done*2}%]")
    sys.stdout.flush()

def Downloader(url):
    try:
        data = YouTube(url,on_progress_callback=progress_func)
        info(data)
        video = data.streams.get_highest_resolution()
        print(f'File Size {video.filesize//(1024*1024)} MB')
        video.download()
        title = str(data.title)
        print(f'\nVideo Sucessfully downloaded at "{path.join(getcwd(),title)}"')
    except Exception as e:
        print('Error occured in downloading your request')
        print(e)

url = input('Enter Video URL : ')
Downloader(url)