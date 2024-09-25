import eyed3
import os
from tqdm import tqdm
from pathlib import Path

folder = input("Please Select Folder: ")
paths = sorted(Path(folder).iterdir(), key=os.path.getmtime)

ARTIST = input('ARTIST: ')
ALBUM =  input('ALBUM : ')

for i in tqdm(range(len(paths))):
    file = str(paths[i])
    # just a short list of parameters to the MP3 File. 
    title = file.split('\\')[-1]
    audiofile = eyed3.load(file)
    audiofile.tag.artist = ARTIST
    audiofile.tag.album = ALBUM
    audiofile.tag.title = title
    audiofile.tag.track_num  = i
    audiofile.tag.save()
