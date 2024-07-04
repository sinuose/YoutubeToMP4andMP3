import pytube
import sys
import os
from utils import *
from yt_scraper import *

if __name__ == '__main__': # only runs when executed as a script
        #print('This will save as an MP4, and MP3')
        output = input('Save Path: ')
        # get the directories ready
        mp4_dir = output + r'\mp4'
        mp3_dir = output + r'\mp3'
        ensure_dir(mp4_dir)
        ensure_dir(mp3_dir)


        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            link = input('Youtube Link:')
            if link == 'quit':
                print('\n See you next time.')
                sys.exit()
            mp4_saved = getYoutubeMP4Highest(link, mp4_dir)
            mp3_saved = mp4_saved.replace('mp4', 'mp3')
            convertMP4toMP3(mp4_saved, mp3_saved)