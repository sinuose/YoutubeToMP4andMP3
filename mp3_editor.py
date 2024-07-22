import eyed3
import os
from tqdm import tqdm

folder = input("Please Select Folder: ")
file_list = os.listdir(folder)

ARTIST = input('ARTIST: ')
ALBUM = input('ALBUM:')

i = 0
for file in tqdm(file_list):
    # just a short list of parameters to the MP3 File. 
    title = file.copy()
    file = folder + '/' + file
    audiofile = eyed3.load(file)
    audiofile.tag.artist = ARTIST
    audiofile.tag.album = ALBUM
    audiofile.tag.title = title
    audiofile.tag.track_num  = i
    audiofile.tag.save()
    i += 1
