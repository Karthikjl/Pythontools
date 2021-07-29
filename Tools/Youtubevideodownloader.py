from pytube import YouTube
from os import getcwd,path,sysconf


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

def progress_func(stream,chunk,):
    
